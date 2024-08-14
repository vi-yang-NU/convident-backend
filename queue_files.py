import os
from speech_analysis_main import set_audio_files, process_data

# Path to the queue.txt file
queue_file = "/Users/viyang/Convident_backend/queue.txt"

# Path to the folder where files will be added
queue_folder = "/Users/viyang/Convident_backend/queue"

# Function to add a file to the queue
def add_to_queue(new_file):
    # Read the existing list of files from the queue.txt file
    with open(queue_file, "r") as file:
        files = file.read().splitlines()
    # Add the new file to the list
    files.append(new_file)
    # Write the updated list of files back to the queue.txt file
    with open(queue_file, "a") as file:
        file.write(new_file + "\n")
    # Move the new file to the queue folder
    new_file_name = os.path.basename(new_file)
    new_file_path = os.path.join(queue_folder, new_file_name)
    # Write the updated list of files back to the queue.txt file
    os.rename(new_file, new_file_path)

# Function to clear the queue.txt file
def clear_queue():
    with open(queue_file, "w") as file:
        file.write("")

def run_post():
    with open("log.txt", "a") as file:
        file.write("the queue has ended, starting post-processing\n")
    # Read the list of files from the queue.txt file
    with open(queue_file, "r") as file:
        files = file.read().splitlines()
    # with open("log.txt", "w") as file:
    #     file.write("\n".join(files))
    # Feed the array of files to prod
    # Save the list of files to log.txt
    
    # with open("log.txt", "a") as file:
    #     file.write("running set_audio_files\n")

    set_audio_files()
    
    # with open("log.txt", "a") as file:
    #     file.write("processing data\n")

    process_data()
    # Clear the queue.txt file
    # with open("log.txt", "a") as file:
    #     file.write("data processed\n")
        
    clear_queue()
