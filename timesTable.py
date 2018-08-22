# Times Tables

# Ask the user to input the number they would like the times tables for
tTable = int(input("What number would you like to see the times table for? "))

# Loop through 12 times
for number in range(12):
    print("{0} times {1} equals {2}" .format(number+1, tTable, (number+1) * tTable))

input()
