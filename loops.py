### While Loop
##count = 0
##while (count < 9):
##   print('The count is: ', count)
##   count = count + 1
##
### For Loop
##charCount = 0
##print("Please input a string")
##testString = input()
##for x in testString:
##   charCount = charCount + 1
##
##print("There are ", charCount, " characters in the string you input")

# For Loop
## Uses an input from the user
userHello = int(input("Please input a number"))
for number in range(userHello):
   print("Hello")

# While Loop
## Checks for what the user inputs and will loop until they type 'stop'
print("Enter some numbers. Type 'stop' to finish\n")
number = 0
while number != 'stop':
   number = input("Enter a number or 'stop': ")
   print(number)

# While Loop
## Password checker
password = input("Please enter a password\n")
print("Please enter your password")
checkPassword = input()
while checkPassword != password:
   checkPassword = input("Incorrect. Please enter your password\n")
print("Access Granted")


print("Good bye!")
input()
