
print ("First calculator!")
print ("")

firstnum=input ("Insert the first number: ")
print ("")
print ("Available operations:\n 1:Addition\n 2:Subtraction\n 3:Multiplication\n 4:Division\n")
operation=input ("Insert the number of operation: ")
if int(operation) >4:
        print ("You mistyped")
        exit(0)
print ("")
secondnum=input ("Insert the second number: ")

firstnum=int(firstnum)
secondnum=int(secondnum)

print ("")
if operation == "1":
    print ("The result is:", firstnum+secondnum)
elif operation == "2":
    print ("The result is:", firstnum-secondnum)
elif operation == "3":
    print ("The result is:", firstnum*secondnum)
elif operation == "4":
    print ("The result is:", firstnum/secondnum)
