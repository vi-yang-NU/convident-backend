from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_push_queue():
    file_1 = {'file': ('Sentence 1.m4a', open('/Users/viyang/Downloads/Sentence 1.m4a', 'rb'), 'audio/m4a')}
    file_2 = {'file': ('Sentence 2.m4a', open('/Users/viyang/Downloads/Sentence 2.m4a', 'rb'), 'audio/m4a')}
    file_3 = {'file': ('Sentence 3.m4a', open('/Users/viyang/Downloads/Sentence 3.m4a', 'rb'), 'audio/m4a')}
    file_4 = {'file': ('Sentence 4.m4a', open('/Users/viyang/Downloads/Sentence 4.m4a', 'rb'), 'audio/m4a')}
    file_5 = {'file': ('Sentence 5.m4a', open('/Users/viyang/Downloads/Sentence 5.m4a', 'rb'), 'audio/m4a')}
    file_6 = {'file': ('Sentence 6.m4a', open('/Users/viyang/Downloads/Sentence 6.m4a', 'rb'), 'audio/m4a')}
    file_7 = {'file': ('Sentence 7.m4a', open('/Users/viyang/Downloads/Sentence 7.m4a', 'rb'), 'audio/m4a')}
    file_8 = {'file': ('Sentence 8.m4a', open('/Users/viyang/Downloads/Sentence 8.m4a', 'rb'), 'audio/m4a')}
    files = [file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8]
    
    for file in files:
        with open("log.txt", 'a') as log_file:
            log_file.write("Uploading new file: " + str(file) + "\n")
        
        response = client.post("/push-queue/", files=file)
        with open("log.txt", 'a') as log_file:
            log_file.write(f"push-queue response: {response.status_code}\n")
        
        response = client.post("/end-queue")
        with open("log.txt", 'a') as log_file:
            log_file.write(f"end-queue response: {response.status_code}\n")
        
        response = client.post("/cleanup")
        with open("log.txt", 'a') as log_file:
            log_file.write(f"cleanup response: {response.status_code}\n")

    # Add more assertions based on what your endpoint returns or does