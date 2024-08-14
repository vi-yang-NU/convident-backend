from deepgram import DeepgramClient
import os
from dotenv import load_dotenv
import json
from pydub import AudioSegment


deepgram = DeepgramClient()
Deepgram_API_KEY = "d879658397c0c1dd8f40ae6713db824efac2f50a"
timestamp_arr = []

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)

def segment_control():
    timestamps = ""
    with open('queue.txt', 'r') as file:
        for line in file:
            AUDIO_FILE = line.strip()
            timestamps = str(timestamps) + str(test_deepgram(AUDIO_FILE)) + "\n"
        with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
                log_file.write("transcript: " + timestamps)
    timestamp_arr.append(timestamps)

# output a tone transcript  
# taking in a file, so using some other software to record a file 
def test_deepgram(AUDIO_FILE):
    try: 
        # input_data is the audio file that we need to split 
        deepgram = DeepgramClient(Deepgram_API_KEY)

        with open(AUDIO_FILE, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }
        
        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            language = "zh"
        )

        # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        #     log_file.write("running deepgram transcription \n")

        # STEP 3: Call the transcribe_file method with the text payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        # print("data: " + str(data))

        timestamps = helper_audio_split(response, AUDIO_FILE)  # Split the audio file based on the response

        # Print the response

        return timestamps

    except Exception as e:
        print(f"Exception: {e}")

# Helper function for test_deepgram - splits the sentence into individual words 
def helper_audio_split(response, AUDIO_FILE):

    # Load your audio file
    audio = AudioSegment.from_file(AUDIO_FILE)
    timestamps = []

    # Load JSON data
    data = json.loads(response.to_json())
    # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
    #     log_file.write("data loaded in helper_audio: ")
    #     log_file.write(str(data))
    #     log_file.write("\n")

    # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
    #     log_file.write("Finding time stamps\n")

    for channel in data["results"]["channels"]:
        for alternative in channel["alternatives"]:
            for word_info in alternative["words"]:
                word = word_info["word"]
                start = word_info["start"] * 1000  # Convert to milliseconds
                end = word_info["end"] * 1000      # Convert to milliseconds
                timestamps.append((word, start, end))

    # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
    #     log_file.write("timestamps loaded\n")

    # Split audio based on timestamps and export each segment
    for word, start, end in timestamps:
        split_audio = audio[start:end]
        # Clean the word to be a valid filename
        clean_word = ''.join(e for e in word if e.isalnum())
        split_audio.export(f"Analysis_backend/split_audio/{os.path.basename(AUDIO_FILE)}_{clean_word}.wav", format="wav")
        # with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        #     log_file.write("audio is actually split" + "\n")

    return timestamps

if __name__ == "__main__":
    segment_control()