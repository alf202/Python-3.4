animals = ['lepoard', 'bear', 'tiger', 'rabbit']
choice = input("Please enter the name of an animal: ")
# print(animals)

'''
#Method 1 - using IN keyword only

if choice in animals:
    print("Found", choice,"using IN animals!")
else:
    print("Sorry",choice,"not found in animals...")
'''

#Method 2 - looping through list using indices and ==
'''
for i in range(len(animals)):
    if choice == animals[i]:
        print(i, "Found", animals[i],"in animals loop!")
'''
#Method 2a- printing the whole list on one line as a shopping list (with correct character spacing
for i in range(len(animals)):
    print(animals[i], end=" ")

