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

def repl(m):
    word = m.group()
    word = word[1:]
    print word       
    return word

text = open("twain.txt")
word_count = {}

for line in text:
    line = line.strip()
    if line:
        words = line.split(" ")
        for i, word in enumerate(words):
            if re.search("^\"$", word):
                del words[i]
            elif re.search("^\"\w*", word):
                re.sub("^\"\w*", repl, word)


text.close()




























