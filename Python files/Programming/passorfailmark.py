exam = [0] * 5
subject = [0] * 5
for i in range(len(exam)):
    exam[i] = int(input("Mark: "))
    subject[i]= input("Subject: ")

for i in range(len(exam)):
    if exam[i] > 50:
        print(exam[i],subject[i],"You have passed. Well done.")
    else:
        print(exam[i],subject[i],"You have failed. You will need to resit.")
        
    
    
