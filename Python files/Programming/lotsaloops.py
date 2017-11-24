x = 10
y = 20

'''
# Task 1

for i in range (1,11):
    print(i, "squared is",  i**2)

#Task 2
for i in range (1,21):
    print(i, "squared is", i**2)
    print(i, "cubed is", i**3)

# Task 3

i = 0
while i != 21:
    print(i, "squared is", i**2)
    print(i, "cubed is", i**3)
    i = i + 1

#Task 4

num = int(input("Please enter a number: "))

print(num, "squared is ", num**2 , "and cubed is ", num**3)


# Task 5

num = int(input("Please enter a number: "))

if num != -1:
    num = int(input("Please enter a number: "))
'''

#Task 6
numinput = 0
numtotal = 0
while numinput != -1:
    numinput = int(input("Please enter a number: "))
    numtotal = numtotal + numinput
    if numinput == -1:
        print("End of program. Your total was", numtotal)

