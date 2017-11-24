choc = "Bounty"

print("Twix", "Bounty", "Mars")
choice = input("Which is your favourite chocolate from the list? ")

'''
## using ==
if choice == choc:
    print("Hey!", choc, "is my favourite too...!")

# using !=
if choice != choc:
    print("Yuk!")
  
## now do with else
if choice == choc:
    print("Hey! That's my favourite too..!")
else:
    print("Yuk! I don't like", choice)
'''

## next do elif
if choice == choc:
    print("Hey! That's my favourite too.")
elif choice == "Twix":
    print("Twix. Hmm 10 of them! too much.")
elif choice == "Mars":
    print("Too gooey.")
