from collections import Counter
def word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    words = text.split()
    frequency = Counter(words)
    return frequency
file_path = 'C:/Users/dinak/Downloads/Q13sample.txt'
frequency = word_frequency(file_path)
print("Word Frequency Distribution:\n", frequency)
