
import re
import sys 

def rmv_front_char(m):
    word = m.group()
    word = word[1:]       
    return word


def rmv_back_2_char(m): 
    word = m.group()
    word = word[:-2]
    return word


def rmv_end(m):
    word = m.group()
    word = word[:-1]
    return word 


def iter_inspect_wrds(words, word_count):
    for i, word in enumerate(words):
        if re.search("^\"$", word):
            del words[i]
            continue 
        elif re.search("^\"\w*", word):
            word = re.sub("^\"\w*", rmv_front_char, word)
        elif re.search("\w+[\.\,\?\)\;\:\!]$", word):
            word = re.sub("\w+[\.\,\?\)\;\:\!]$", rmv_end, word)
        elif re.search("\w+[\.\,\?\)\;\:\!]\"$", word): 
            word = re.sub("\w+[\.\,\?\)\;\:\!]\"$",rmv_back_2_char, word)
        elif re.search("\w+\"$", word): 
            word = re.sub("\w+\"$", rmv_end, word)

        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1


def count_words_dict(text):
    word_count = {}
    count = 0
    for line in text:
        line = line.strip()
        if line:
            words = line.split(" ")
            iter_inspect_wrds(words, word_count)

    return word_count


def print_word_count(word_dict): 
    for word, count in word_dict.items():
        print "{} {}".format(word, count)


filename = sys.argv[1]

if filename:
    text = open(filename)

words = count_words_dict(text)
print_word_count(words)

text.close()