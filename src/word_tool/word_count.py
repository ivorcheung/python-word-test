def count_words_in_sentence(sentence):
    return len(sentence.split())

def count_number_of_sentences(text):
    return text.count(".")

def find_longest_word_length(sentence):
    return len(max(sentence.split(), key=len))