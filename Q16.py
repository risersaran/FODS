from collections import Counter
def word_frequency_in_reviews(file_path):
    with open(file_path, 'r') as file:
        reviews = file.read().lower()
    words = reviews.split()
    frequency = Counter(words)
    return frequency
file_path ="C:/Users/dinak/Downloads/Q16sample.txt"
frequency = word_frequency_in_reviews(file_path)
print("Word Frequency Distribution:\n", frequency)
