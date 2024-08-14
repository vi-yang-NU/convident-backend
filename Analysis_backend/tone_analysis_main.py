import numpy as np
from Analysis_backend.segment_audio_to_words import segment_control
from Analysis_backend.get_transcript import get_tone_transcript_by_id
from Analysis_backend.tone_compare import tone_compare
from Analysis_backend.pitch_analysis import tone_control
from Analysis_backend.cleanup import cleanup

search_id = 0
audio_file = "/Users/viyang/Convident_backend/fake_audio.m4a"

# Function to push ID
def pushID(value):
    global search_id
    search_id = value

# Function to push audio_file
def pushAudioFile(value):
    global audio_file
    audio_file = value

def process():
    #get the accurate tone transcript from the csv file
    global search_id
    search_id = 1 # hard coding search ID 
    
    # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
    #     log_file.write("getting tone transcript\n")

    tone_transcript = get_tone_transcript_by_id(search_id, audio_file)

    # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
    #     log_file.write("tone transcript received\n")

    with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        log_file.write("Correct tone transcript" + str(tone_transcript) + "\n")

    #seperate the audio file into smaller chunks

    segment_control()

    # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
    #     log_file.write("audio seperated\n")

    # run pitch which returns the tones of the audio file
    user_tones = tone_control(search_id, audio_file)
    with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        log_file.write("user's tone transcript'\n")
        log_file.write(str(user_tones) + "\n")
    #compare the two

    red_lined_words = tone_compare(tone_transcript, user_tones, search_id)

    with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        log_file.write("tones compared \n")

    with open('/Users/viyang/Convident_backend/results.txt', 'a') as results_file:
        results_file.write(str(red_lined_words) + "\n")
    
    #red_lined_words has two return parameters red_lined_words.similarity_percentage and red_lined_words.words
    
    cleanup()

    return red_lined_words; 