import string
import random
WORDLIST_FILENAME = "words.txt"
def load_words():

    print("loading word list from file ....")
    infile = open(WORDLIST_FILENAME,"r")
    line = infile.readline()
    word_list = line.split()
    print(" ",len(word_list), "words loaded . \n\n")
    return word_list

def choose_word():
    
    return random.choice(word_list)
word_list = load_words()