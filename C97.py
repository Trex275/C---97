#Write a program to count the number of words in the input by user
userinput = input("Enter any sentence :")
print(userinput)
numberofwords = 1
numberofcharachters = 0
for i in userinput: 
    if i==' ': 
        numberofwords = numberofwords + 1
    else: 
        numberofcharachters = numberofcharachters + 1

print("number of words in input string is")
print(numberofwords)
print("number of charachters in input string is")
print(numberofcharachters)