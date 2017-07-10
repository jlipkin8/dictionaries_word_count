# put your code here.
poem = open("twain.txt")
word_counts = {}

for line in poem:
    line = line.rstrip()
    words = line.split(" ")

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print "{} {}".format(word, count)

poem.close()
