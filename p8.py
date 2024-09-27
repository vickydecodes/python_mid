#wordcount -1 program

file = open('./txt', 'r')

wordcount = {}

for word in (file.read()).split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
        
print(wordcount)