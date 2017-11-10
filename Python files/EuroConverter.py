'''
money = float(input("Please enter the amount of pounds that you wish to convert:"))

newmoney = money * 1.13

print("For £",money, "you would get",round(newmoney,2),"euros.")
'''
#Conversion Rates
europound = 0.88
poundeuro = 1.13

n#User input to ask euro to pound or pounds to euro
convert = input("Do you wish to convert from pounds to euro or from euro to pounds? ")

if convert == "euro": #Euros to pounds
    euromoney = float(input("Please enter the number of euros that you wish to convert: "))
    neweuromoney = euromoney / europound
    print("You would have £", round(neweuromoney,2),)
elif convert == "pounds": # Pounds to Euros
    poundmoney = float(input("Please enter the number of pounds that you wish to convert: "))
    newpoundmoney = poundmoney * poundeuro
    print("You would have", round(newpoundmoney,2), "euros") # Rounding float down to two decimal places
else: #Neither pounds or euros
    print("Please restart this program.")
    
