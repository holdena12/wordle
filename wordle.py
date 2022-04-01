import random

# splits a word into indivual characters
def splitWord(word):
    return [char for char in word]

# strips a list of words from any end of line tokens like \n
def stripWords(wordList):
    count = 0
    validWords = set()
    for line in wordList:
        count += 1
        validWords.add(line.strip().lower())
    return validWords

# reads a file which is expected to be a list of words seperated by new lines
def readFile(fileName):
    # read dictionary and assign to lines
    with open(fileName) as f:
        lines = f.readlines()
        strippedWords = stripWords(lines)
    f.close()
    return strippedWords

#the set of all valid words that a player may guess
validWords = readFile('dict.txt')

#load a set of potential answer words

answerWords=readFile('words.txt')


    #print(f'word {count}: {line}')

# get an input from user to indicate easy or hard mode
hardMode = input('do you want to play on hard mode, Enter yes if so: ').lower()
# if easy mode, use 'answerWords' for ansewr, if hard use validWords  
answer=''
if (hardMode=='yes'):
    anwser=random.choice(list(validWords))
# select random word from dictinary
else:
    anwser=random.choice(list(answerWords))
#print(anwser)

# read input from user to get test word
solved = False
for i in range(6):
    if (solved):
        break
    while True:
        wordChoice = input('Enter Guess: ').lower()
        if wordChoice in validWords:
            print('valid word entered')
            charPos = 0
            for c in splitWord(wordChoice):
                
                # print 2 if the character is in the answer AND in the correct spot
                # print 1 if the character is in the answer but not in correct spot
                # print 0 if the character is not in the answer
                if (c in anwser):
                    # if the char in position charPos in answer = 0 print 2, else print 1
                    if (c == anwser[charPos]):
                        print(f'{c}:2')
                    else:
                        print(f'{c}:1')
                else:
                    print(f'{c}:0')
                charPos += 1
            if wordChoice==anwser:
                solved = True
                print ('you have succsefully completed this make shift wordle!')
            break;
        else:
            print('invalid word, try again')
#else input not in (valid_words)):
#    print('not in wordlist try something else(:.')

if (solved == False):
    print(f'sorry, the answer was : {anwser}')


    
