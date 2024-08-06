# 1. **Add two numbers**

#    Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1: Prompt the user to enter the first number
first_number_input = input("Enter the first number: ")

# 2: Read the input and convert it to an integer
first_number = int(first_number_input)

# 3: Prompt the user to enter the second number
second_number_input = input("Enter the second number: ")

# 4: Read the input and convert it to an integer
second_number = int(second_number_input)

# 5: Calculate the sum of the two numbers
sum_of_numbers = first_number + second_number
print("The sum of the two numbers is:", sum_of_numbers)


# 2. **Agreement Boot**

#    Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also \_\_\_!" (the blank should be filled in with the user-inputted animal, of course).

favorite_animal: str = input("What's your favorite animal? ")

if favorite_animal.strip():
    print(f"My favorite animal is also {favorite_animal}!")
else:
    print("You didn't enter an animal.")


