import openai
import random
import csv
import speech_analysis_main as prod


def retrieve_conversation():
    conversation_id = random.randint(1, 2)
    conversation_id = 1 # hard coding this for now to test the functionality
    dialogue = []
    prod.save_convo_ID(conversation_id)

    with open('/Users/viyang/Convident_backend/Conversation speadsheet.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(conversation_id):
                dialogue.append(row[1])

    return dialogue
