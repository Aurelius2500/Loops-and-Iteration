# -*- coding: utf-8 -*-
"""
For Loops, while loops, and more looping and iteration with Python
Spyder version 5.3.3
"""

# This video is a follow-up to the Absolute Programming Basics with Python video
# We will refresh our procedual programming basics first
# Compare two numbers to get a boolean
 
first_variable = 6

second_variable = 8

# Use the if else statement to compare them
# This is the simplest way to see the control flow in action
# We can think of the control flow as a more advanced order of operations

if first_variable > second_variable:
    print("The value of the first variable is higher than the value of the second variable")
else:
    print("The value of the second variable is higher than the value of the first variable")
    
# Now, let's change the first variable to 15

first_variable = 15

# Execute the same if else statement after storing the new variable
# Notice that the statement that was print was the else part of the statement, because the condition was not met
# We are skipping the statement if the condition is true, and going to the part where it is false

# Recall that lists are variables with multiple items inside them
programming_languages = ["Python", "R", "Java", "Ruby", "Julia"]
print(programming_languages)

# We can access any of the individual items by using an index
print(programming_languages[0])

# And see how many items are inside a list
print(len(programming_languages))

# A while loop allows us to execute code with a condition that will terminate the loop if it is not true
# Let's start by printing 10 "This is a loop" statements
i = 0
while i <= 9:
    print("This is a while loop")
    
# Notice how the loop goes and it doesn't stop
# This is due because i is 0, and it will keep being less than 9
# However, we can use i = i + 1 to control this and increase i by 1 every time that we go through the loop
i = 0
while i <= 9:
    print("This is another while loop")
    i = i + 1
    
# Or as an abbrevation available in Python, i += 1
i = 0
while i <= 9:
    print("This is a third while loop")
    i += 1
    
# We could also print the items inside the list using list iteration
i = 0
while i <= len(programming_languages):
    print(programming_languages[i])
    i += 1
    if i == len(programming_languages):
        print("Stop the while loop")
        break
    
# Let's do a small demonstration of the power of while loops: a simple door game
i = 0
while i == 0:
    print("Welcome to this simple video game")
    print("Do you want to go through door 1 or 2?")
    door = int(input("Please type either 1 or 2: "))
    print(f"You have chosen door {door}")
    if door == 1:
        print("Congratulations! You have won")
        i = 1
    elif door == 2:
        print("Sorry, you have lost")
        i = 1
    else:
        print("Output not valid, try again")
        print("Game is restaring...")
        print("")
        
# We can see that we first ask the user to either choose door 1 and 2, and then execute the statements inside them
# If the user gives an input that it is not valid, then we just go back to the beginning
# While loops are awesome to keep something going until it is not true anymore
# A lot of video games are pretty advanced for and while loops

# For loops are useful to go through iterations of an object
for i in range(len(programming_languages)):
               print(programming_languages[i])

# i is an rather arbitraty convention, but it stands for index, we could use any other valid variable name
# We can also iterate through a string
new_string = "This is a string"

for letter in new_string:
    print(letter)
    
# We can elaborate a lot more inside the for loops, getting very fancy outputs
# The loop below does the same thing as the loop above, but in a more sophisticated way
let_num = 1
for letter in new_string:
    print(f"This is letter number {let_num} of the string: {letter}")
    let_num += 1
    if let_num == 17:
        print(f"This is the end of the string with a length of {len(new_string)}")
        
# This is especially important in running machine learning models, as we can produce more structured outputs

# Finally, let's demonstrate the power of for and while loops by putting for loops in our door game
# We will add a verification to see if the user can go back to the game
i = 0
sum_numbers = [2, 5, 12]
while i == 0:
    print("Welcome to this simple video game")
    print("Do you want to go through door 1 or 2?")
    door = int(input("Please type either 1 or 2: "))
    print(f"You have chosen door {door}")
    if door == 1:
        print("Congratulations! You have won")
        i = 1
    elif door == 2:
        print("Sorry, you have lost")
        i = 1
    else:
        print("Output not valid, if you want to try again, input the correct sum of the following numbers")
        for number in range(len(sum_numbers)):
            print(sum_numbers[number])
        sum_user = int(input("Plese type the sum of the numbers: "))
        if sum_user == sum(sum_numbers):
            print("...")
            print("Thinking...")
            print("You are back in the game!")
        else:
            print("Sorry, that is not correct, you are out of the game")
            i = 1
    if i == 0:
        print("Game is restaring...")
    else:
        print("Game is over")
    print("")
        
# Now, imagine combining this with functions, procedual programming is a powerful tool for both analytics and automation
# You can do almost anything in a while loop, and then just come back at it by restarting the loop