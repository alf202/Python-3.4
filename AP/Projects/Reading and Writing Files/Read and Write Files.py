#First block of code creates a file with the lines
'''
Some Text
I love Python!
'''
fw = open('sample.txt', 'w')
fw.write('Some Text\n')
fw.write('I love Python!\n')
fw.close()

#Second block of code reads the file then gives then prints the output

fr =open('sample.txt', 'r')
text = fr.read()
print(text)
