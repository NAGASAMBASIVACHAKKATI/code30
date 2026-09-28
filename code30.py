sentence=input()
words=sentence.split()
for i in range(len(words)-1,-1,-1):
    print(words[i][::-1],end=" ")
