import random

def splitWord(word):
    return [char for char in word]

 # read dictionary and assign to lines
with open('dict.txt') as f:
    lines = f.readlines()
f.close()

# print lines in file
count = 0
validWords = set()
for line in lines:
    count += 1
    validWords.add(line.strip())
    #print(f'word {count}: {line}')  
# select random word from dictinary
anwser=random.choice(list(validWords))
#print(anwser)

# read input from user to get test word
solved = False
for i in range(6):
    if (solved):
        break
    while True:
        wordChoice = input('Enter Guess: ')
        if wordChoice in validWords:
            print('valid word entered')
            charPos = 0
            for c in splitWord(wordChoice):
                
                # print 1 if the character is in the answer AND in the correct spot
                # print 2 if the character is in the answer but not in correct spot
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


    
