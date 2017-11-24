'''
# string length
str1 = "computer"
print(len(str1))

print(str1[3])

print(str1[6],str1[5],str1[4],str1[3],str1[2],str1[1])
'''

# split() function to break into smaller things
str2 = "computer science is cool"
strSplit = str2.split()
print(strSplit)

print(strSplit[3], strSplit[1], strSplit[2], strSplit[0])
# use join() to rejoin broken string to one string
print(' '.join(strSplit))
      

# strip() to remove things from start or end of string
str3 = "      ,,,,this is a test,"
print(str3)
print(str3.strip(' ,'))


#lower(), upper() & title() to convert case
str4 = "Computer Science"

print(str4.lower())
print(str4.upper())

str5 = "alfie payne"

print(str5.title())
