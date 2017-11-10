import random #Imports the random library

num = random.randint(1,100) # determining the number for the user to guess 
print(num) # in development mode, printing the number

numgess = 0 # starting number of guesses
guess = int(input("Please enter your guess: ")) # Asking for the first gues
numgess = numgess + 1 # incrementing the numgess
while guess != num: # starts while loop if the input is not the number
    if guess > num: # if the input is higher than the number
        print("Too high") # prints this if the number is too high
        numgess = numgess + 1 # increments the guesses
    elif guess < num: # if the guess is smaller than the number
        print("Too low") # prints this if the number is too low
        numgess = numgess + 1 # increments the numguess variable
    guess = int(input("Please enter your guess: ")) # asking for another input
print("Correct!, you did it in ", numgess, "guess(es)") # when user gets it correct, the user is told that they have gotten it correct, and prints the number of guesses they got it in.

