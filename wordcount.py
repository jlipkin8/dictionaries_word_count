
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


def count_word(wrd):
    word = wrd.lower()
    word_count[word] = word_count.get(word, 0) + 1


def iter_inspect_wrds(words):
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

        count_word(word) 


filename = sys.argv[1]

if filename:
    text = open(filename)

word_count = {}
count = 0

for line in text:
    line = line.strip()
    if line:
        words = line.split(" ")
        iter_inspect_wrds(words)


# for word, count in word_count.items():
#     print "{} {}".format(word, count)
# text.close()