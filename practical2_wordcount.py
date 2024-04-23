#this file needs a txt file to run it is named as practical2.txt
import re    #regular expression module 
from multiprocessing import Pool  #module to run mapper and reduced function simultaneously

WORD_RE = re.compile(r"[\w']+") 

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def mapper(line):
    word_count = {}
    for word in WORD_RE.findall(line):
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    return word_count

def reducer(mapped_counts):
    reduced_counts = {}
    for word_count in mapped_counts:
        for word, count in word_count.items():
            reduced_counts[word] = reduced_counts.get(word, 0) + count
    print(reduced_counts)
    return reduced_counts


def main(filename, target_word):
    lines = read_file(filename)

    # Use multiprocessing to parallelize mapping
    with Pool() as pool:
        mapped_counts = pool.map(mapper, lines)

    # Reduce the mapped counts
    reduced_counts = reducer(mapped_counts)

    # Get the frequency of the target word
    target_frequency = reduced_counts.get(target_word.lower(), 0)

    print(f"The frequency of '{target_word}' in the file is: {target_frequency}")

if __name__ == "__main__":
    filename = input("Enter the file path: ")   #paste the path of practical2.txt, after running the code 
    target_word = input("Enter the word to find frequency: ")  #enter any word fro practical2.txt
    main(filename, target_word)
