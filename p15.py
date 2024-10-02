#wordcount 2

file = open('D:/Documents/semesterpy/txt3.txt', 'r')

wordcount = {}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print(wordcount)

maxno = 5

for key in wordcount.keys():
    if wordcount[key] > maxno:
        maxno = wordcount[key]


for key in wordcount.keys():
    if wordcount[key] == maxno:
        print(key)
        
        
