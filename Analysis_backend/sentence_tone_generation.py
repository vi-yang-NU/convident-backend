# this file only needs to be called if the CSV file does not have a tone transcript, so this file will not be used
import openai

openai.api_key = 'sk-proj-wDOImEzEihv26aM2yfliT3BlbkFJC3SBK9CtuXzvHAdPFIRh'

prompt = "Generate the tones for the following sentence using only the symbols -, /, V, . If the input was 你好吗, your output should be 'V V -'. Here is the input sentence:" + "你好吗"

# tone_transcript = ["\\", "/", "V", "V", "-", "-", "/", "V", "\\", "-"] # tone transcript of the audio file
#tone_transcript = ["/", "V", "V", "/", "-", "/", "V", "V", "-", "-", "/", "-", "\\", "/", "-", "-", "/", "/", "V", "-", "-", "/", "-", "\\"] # tone transcript of the audio file
# [{"A", "-"}, {"B", "/"}, {"C", "V"}, {"D", "\\"}]

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-004",  # You can specify the model here, such as "text-davinci-003" or "gpt-4"
        prompt=prompt,
        max_tokens=150,  # Adjust the max tokens as per your requirement
        n=1,
        stop=None,
        temperature=0.7  # Adjust the temperature for more/less creative responses
    )

    # do response cleaning, so that the response is only the tones

    return response.choices[0].text.strip() # make sure the output is in an array format ["", "", "", "", ""]
