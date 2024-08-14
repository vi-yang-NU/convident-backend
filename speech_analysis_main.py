import pandas as pd
from Analysis_backend.tone_analysis_main import pushID, pushAudioFile, process
import os


# process_data.py
convo_ID = 0
paths_to_files = []
queue_folder = "/Users/viyang/Convident_backend/queue"
log_path = '/Users/viyang/Convident_backend/log.txt'
queue_file = "/Users/viyang/Convident_backend/queue.txt"


# def dummy_method():
#     with open(log_path, 'a') as log_file:
#             log_file.write("dummy method\n")

def set_audio_files():
    # get the list of audio files in the queue folder
    audio_files = os.listdir(queue_folder)
    global paths_to_files
    paths_to_files = [os.path.join(queue_folder, file) for file in sorted(audio_files) if not file.startswith('.')]
    
    # with open(log_path, 'a') as log_file:
    #     log_file.write(f"{paths_to_files}\n")
    # Write the updated list of files back to the queue.txt file
    with open(queue_file, 'w') as queue_txt:
        queue_txt.write('\n'.join(paths_to_files))


def process_data():
    #TODO
    global convo_ID
    convo_ID = 1 # hard coding this, fix this in future 
    # with open(log_path, 'a') as log_file:
    #     log_file.write("pushing ID\n")
    pushID(convo_ID)                                        
    for file in paths_to_files:
        # with open(log_path, 'a') as log_file:
        #    log_file.write("pushing file\n")
        pushAudioFile(file)
        # with open(log_path, 'a') as log_file:
        #    log_file.write("processing\n")
        process()
        # with open(log_path, 'a') as log_file:
        #    log_file.write("finished processing\n")

def save_convo_ID(convo_id):
    global convo_ID
    convo_ID = convo_id




# takes in sentences and creates a list of the sentences/ what was right and wrong for the entire dialogue