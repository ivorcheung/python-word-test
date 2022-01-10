from collections import Counter

def count_words_in_sentence(sentence):
    return len(sentence.split())

def count_number_of_sentences(text):
    return text.count(".")

def find_longest_word_length(sentence):
    return len(max(sentence.split(), key=len))

def find_six_most_recurring_words(sentence):
    recurring = Counter(sentence.split())
    return recurring.most_common(6)

def find_percentage_of_words_occuring_once(sentence):
    c = Counter(sentence.split(' '))
    total = sum(c.values())
    return {k: v/total for k, v in c.items()}