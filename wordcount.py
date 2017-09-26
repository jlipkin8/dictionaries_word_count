# put your code here.
# poem = open("twain.txt")
# word_counts = {}

# for line in poem:
#     line = line.rstrip()
#     words = line.split(" ")

#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1

# for word, count in word_counts.items():
#     print "{} {}".format(word, count)

# poem.close()
import re

def rmv_front_char(m):
    word = m.group()
    word = word[1:]       
    return word

def rmv_back_2_char(m): 
    word = m.group()
    word = word[:-2]
    return word

def rmv_end(m):
    print "rmv_end " 
    word = m.group()
    word = word[:-1]
    return word 

def check_word(wrd):
    word = wrd.lower()
    word_count[word] = word_count.get(word, 0) + 1 

text = open("twain.txt")
word_count = {}
count = 0

for line in text:
    line = line.strip()
    if line:
        words = line.split(" ")
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
            else: 
                print word

            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1 


# for word, count in word_count.items():
#     print "{} {}".format(word, count)
text.close()




























re.sub("\w+\"$", rmv_end, word)