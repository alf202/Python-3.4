'''
Author: Alfie Payne
Date: 6th October 2017
Python: 3.4.0
Objective: convert the incorrect sentence gramatically correct.
'''

# Trial and error Code:
'''
incorrect = "   ,tHe capital CITY of The uk is lonDon. "
print(incorrect)
print(incorrect.strip(' ,'))
print(incorrect.upper())
print(incorrect[1])

s1 = ",tHe capital CITY of The uk is lonDon."
print(s1)
s2 = s1.lower()
print(s2)

s2strip = s1.strip(' ,')
print(s2strip)

# s3strip = s2strip.lower()
# print (s3strip)

# s4split = s3strip.split()

s4split = s3strip.split('')
print(s4split)

s5 = s4.split()
s5[1] = s5[1].title()
print(s4)

'''

# The inital sentence that needs to be corrected
s1 = ",tHe capital CITY of The uk is lonDon."
print(s1) # printing the inital sentence

s2 = s1.lower() # makes the whole sentence lower case
print(s2) # printing the lower version

s3 = s2.strip(' ,') # striping the sentence of commas
print(s3) # printing the variable s3

s4 = s3.split() # spliting the sentence, so that each word can be altered
s4[5] = s4[5].upper() # making the 4th word upper case (in this case Uk to UK)
s4[0] = s4[0].title() # making the 1st word titled (in this case the to The)
s4[7] = s4[7].title() # making the 6th word titled (in this case london to London)

s5 = ' '.join(s4) # joining s4 to make new variable s5
print(s5) # printing s5


