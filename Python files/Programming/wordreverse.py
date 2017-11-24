wordToReverse = input("Please enter the word that you wish to reverse: ")

'''
for i in range(len(wordToReverse), -1):
    print(wordToReverse[i],end="")

for i in range(-1,len(wordToReverse), 10):
    print(wordToReverse[i],end="")
'''

for i in range(len(wordToReverse)-1, -1, -1):
    print(wordToReverse[i],end="")
    
