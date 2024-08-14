import parselmouth
import numpy as np
import os
import csv
import re


# determine tone takes in ONE audio file, and then returns the tone of the ONE audio file. 
def determine_tone(audio_file): 
    snd = parselmouth.Sound(audio_file)
    pitch = snd.to_pitch()
    pitch_values = pitch.selected_array['frequency']
    pitch_values = pitch_values[pitch_values > 0]
    if len(pitch_values) == 0:
        return "\0"
    average_pitch = np.mean(pitch_values)
    if average_pitch > 300 or average_pitch < 100: 
        return "\0"
    elif average_pitch > 253 and average_pitch <= 300: 
        return "-"
    elif average_pitch > 240 and average_pitch <= 253: 
        return "\\"
    elif average_pitch > 206 and average_pitch <= 240: 
        return "/"
    else: 
        return "V"
def find_tone_transcript_by_id(target_id):
    with open("/Users/viyang/Convident_backend/Conversation speadsheet.csv", 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['ID'] == str(target_id):
                return row['dialogue script']
    return None

def filter_speaker_b_dialogue(text):
    # Split the text into lines
    lines = text.split('\n')
    # Filter lines that start with "Speaker B (Customer):"
    filtered_lines = [line for line in lines if line.strip().startswith('Speaker B (Customer):')]
    # Join the filtered lines back into a single string
    return '\n'.join(filtered_lines)

def filter_colon_newline(text):
    filtered_text = re.sub(r'[^\u4e00-\u9fff\n]', '', text)
    return filtered_text

def tone_control(search_id, audio_file):
    doc_tone_transcript = find_tone_transcript_by_id(search_id)
    filtered_dialogue = filter_speaker_b_dialogue(doc_tone_transcript)
    filtered_2 = filter_colon_newline(filtered_dialogue)
    with open("/Users/viyang/Convident_backend/Analysis_backend/dialogue.txt", "w") as file:
        file.write(filtered_2)
    filtered_2_array = filtered_2.split('\n')
    audio_file_name = audio_file.split('/')[-1]
    audio_number = int(audio_file_name.split(' ')[-1].split('.')[0])
    #adjusting to make sure the numbers are consistent/ numberings are a bit different 
    audio_number -= 1 

    accuracy = []
    counter = 1
    for character in filtered_2_array[audio_number].strip():
        file_name = f"Sentence {counter}.m4a_{character}.wav"
        file_path = f"/Users/viyang/Convident_backend/Analysis_backend/split_audio/{file_name}"
        # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        #     log_file.write("sentence audio split: ")
        #     log_file.write(str(file_path) + "\n")
        if os.path.exists(file_path):
            tone = determine_tone(file_path)
            accuracy.append(tone)
        else:
            accuracy.append(" na ")
    counter += 1
    accuracy.append("\n")
    return accuracy

# if __name__ == "__main__":
#     accuracy_rate = tone_control(1)
    # print(accuracy_rate)