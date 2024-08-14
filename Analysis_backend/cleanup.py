import os

split_audio_dir = '/Users/viyang/Convident_backend/Analysis_backend/split_audio'
queue_dir = '/Users/viyang/Convident_backend/queue'
log_path = '/Users/viyang/Convident_backend/log.txt'

def cleanup():
    # with open(log_path, 'a') as log_file:
    #     log_file.write("cleanup was called\n")
    
    # Ensure directories exist and then remove directory 1 split audio content
    if os.path.exists(split_audio_dir):
        for filename in os.listdir(split_audio_dir):
            file_path = os.path.join(split_audio_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    # with open(log_path, 'a') as log_file:
                    #     log_file.write(f"deleted: {file_path}\n")
            except Exception as e:
                with open(log_path, 'a') as log_file:
                    log_file.write(f"error deleting: {file_path}: {e}\n")
    
    # Ensure directories exist and then remove directory 2 queue content
    if os.path.exists(queue_dir):
        for filename in os.listdir(queue_dir):
            file_path = os.path.join(queue_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    # with open(log_path, 'a') as log_file:
                    #     log_file.write(f"deleted: {file_path}\n")           
            except Exception as e:
                with open(log_path, 'a') as log_file:
                    log_file.write(f"error deleting: {file_path}: {e}\n")
    else:
        with open(log_path, 'a') as log_file:
            log_file.write("could not find queue directory\n")
    
    # Clearing queue.txt content
    file_path = '/Users/viyang/Convident_backend/queue.txt'
    try:
        if os.path.isfile(file_path):
            with open(file_path, 'w') as file:
                file.write('')
            # with open(log_path, 'a') as log_file:
            #     log_file.write(f"deleted: {file_path}\n")
    except Exception as e:
        with open(log_path, 'a') as log_file:
            log_file.write(f"error deleting queue.txt: {file_path}: {e}\n")
    
    # Clearing dialogue.txt content
    file_path = '/Users/viyang/Convident_backend/Analysis_backend/dialogue.txt'
    try:
        if os.path.isfile(file_path):
            with open(file_path, 'w') as file:
                file.write('')
            # with open(log_path, 'a') as log_file:
            #     log_file.write(f"deleted: {file_path}\n")
    except Exception as e:
        with open(log_path, 'a') as log_file:
            log_file.write(f"error deleting dialogue.txt: {file_path}: {e}\n")