"""The main goal of this project is to count repeated words, to show total and unique words in 
an text file and save the results in new text file"""

import operator

# read the file
file = open("words.txt", "r")

text = file.read()

file.close()

# count the words
words = {}

for word in text.split():
    if word.lower() in words:
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1

# sort the dictionary
sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)

# create new file
file = open("words-count.txt", "w")

# write total and unique words in file
file.write("Total Words in file - {}\n\nUnique Words in file- {}\n\n".format(len(text.split()), len(sorted_words)))

# write count of how many times words are repeated
file.write("Word - Count\n")
for i in sorted_words:
    file.write(f"{i[0]} - {i[1]}\n")

