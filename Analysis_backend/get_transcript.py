import pandas as pd
log_path = '/Users/viyang/Convident_backend/log.txt'


# Function to get tone transcript by ID
def get_tone_transcript_by_id(search_id, audio_file):
    csv_file_path = '/Users/viyang/Convident_backend/Conversation speadsheet.csv'
    df = pd.read_csv(csv_file_path)
    # Find the row with the specified ID
    row = df[df['ID'] == search_id]
    
    # Check if the row exists
    if not row.empty:
        # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        #  log_file.write("tone transcript " + row['tone transcript'].iloc[0])
        # Return the tone transcript
        transcript = row['tone transcript'].iloc[0]
        audio_file_name = audio_file.split('/')[-1]
        number = int(audio_file_name.split(' ')[-1].split('.')[0])
        # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        #     log_file.write("single_sentence_tran number ")
        #     log_file.write(str(number) + "\n")
        single_sentence_tran = transcript_generator(number, transcript)
        

        return single_sentence_tran
    else:
        return "ID not found."

def transcript_generator(number, transcript): 
    # Split the transcript into an array of lines
    lines = transcript.split('\n')

    # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
    #     log_file.write("lines ")
    #     log_file.write(str(lines) + "\n")

    # Access the specified line if it exists
    if 1 <= int(number) <= len(lines):
        # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        #     log_file.write("final returned thing ")
        #     log_file.write(str(lines[number - 1].split()))
        return lines[number - 1].split()
    else:
       return "Line number out of range."
    

