def compare_lists(tone_transcript_split, user_tones_split):
    # Ensure both lists are of the same length for comparison
    min_length = min(len(tone_transcript_split), len(user_tones_split))
    matches = sum(1 for i in range(min_length) if tone_transcript_split[i] == user_tones_split[i])
    
    # Calculate similarity percentage based on the total elements in tone_transcript
    similarity_percentage = (matches / len(tone_transcript_split)) * 100
    
    # Identify words in tone_transcript that do not match with user_tones
    words_not_in_common = []
    wrong_vocab_positions = []
    for i in range(len(tone_transcript_split)):
        if i >= min_length or tone_transcript_split[i] != user_tones_split[i]:
            words_not_in_common.append(tone_transcript_split[i])
            wrong_vocab_positions.append(i)
    
    return similarity_percentage, words_not_in_common, wrong_vocab_positions

def tone_compare(tone_transcript,user_tones, search_id):
    with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        log_file.write("starting compare_lists \n")
    # compare the two lists and return the percentage of similarity
    tone_transcript_split = [word for word in tone_transcript if word != " "]

    results = compare_lists(tone_transcript_split, user_tones)
    # print(f"Similarity percentage: {compare_lists.similarity_percentage}%")
    with open('/Users/viyang/Convident_backend/log.txt', 'a') as log_file:
        log_file.write("compare_lists percent similarity: " + str(results[0])+ "\n")
        log_file.write("words not in common: " + str(results[1]) + "\n")
        log_file.write("wrong vocab positions" + str(results[2]) + "\n")
    
    return results

# if __name__ == "__main__":
#     tone_transcript = '''
#     - V -
#     \ - /
#     '''
#     user_= '''
#     V V -
#     - V -
#     '''

#     search_id = 1
#     result = tone_compare(tone_transcript, user_tones, search_id)
#     print(f"Similarity percentage: {result[0]}%")
#     print(f"Words not in common: {result[1]}")