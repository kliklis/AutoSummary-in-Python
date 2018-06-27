t = input("Welcome to AutoSummary!\nGive the name of the file you wish to summarize.\n")
f = open(t,"r")
s = f.read()

rf = int(input("Give the reduction factor(e.g. 2 subdivides the initial text's size).\n"))
wordSet = []
wordsRanks = []

sentencesList = s.split('.')
L = len(sentencesList)
sentencesRanks = []

print("\n_______________________________________________________")

for i in sentencesList:
    wordBuf = i.split()
    for j in wordBuf:
        if(j not in wordSet and len(j)>3):
            wordSet.append(j)
            wordsRanks.append(s.count(j))
        elif(j not in wordSet and len(j)<=3 and j.isupper() and not j.isnumeric() ):
            wordSet.append(j)
            wordsRanks.append(s.count(j))

for i in sentencesList:
    rank = 0
    wordBuf = i.split()
    for j in wordBuf:
        if(j in wordSet):
            rank = rank + wordsRanks[wordSet.index(j)]
    sentencesRanks.append(rank)

sentencesList = [x for _,x in sorted(zip(sentencesRanks,sentencesList),reverse=True)]

for i in range(len(sentencesList)//rf):
    print(sentencesList[i],end='. ')

print("\n_______________________________________________________\nThe above summary contains: "+str(L//rf)+" out of "+str(L)+" sentences.\n")
