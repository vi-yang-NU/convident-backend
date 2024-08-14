# main.py
from fastapi import FastAPI, HTTPException, File, UploadFile
from retrieve_conversation import retrieve_conversation as rec_conv
from queue_files import add_to_queue, run_post
from Analysis_backend.cleanup import cleanup
import os 

app = FastAPI()

# TODO scale this for multiple users 
# TODO host this on Heroku 

@app.post("/make-conversation")
def make_conversation_endpoint():
    try:
        dialogue = rec_conv()
        return {"dialogue": dialogue}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/push-queue/")
async def push_queue(file: UploadFile = File(...)):
    try:
        # Save the file
        file_path = f"queue/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        add_to_queue(file)

        # Delete the file from the temp directory
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise HTTPException(status_code=404, detail="File not found")

        # return {"filename was uploaded successfully": file.filename}
        return {"status": "200 OK"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/end-queue")
def end_queue():
    try:
        run_post()
        return {"queue was cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/cleanup")
def cleanup_main():    
    try:
        cleanup()
        return {"queue was cleared successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))