# Problem 1:

def compute_ages():
    anton_age = 21
    beth_age = anton_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anton_age
    ethan_age = chen_age

    return {
        'Anton': anton_age,
        'Beth': beth_age,
        'Chen': chen_age,
        'Drew': drew_age,
        'Ethan': ethan_age
    }

# Print the results
ages = compute_ages()
for friend, age in ages.items():
    print(f"{friend} is {age}")


# Problem 2:

name = "Alice"
age = 30
city = "New York"

sentence = f"{name} is {age} years old and lives in {city}."
print(sentence)


# Problem 3:
s = "hElLo WoRlD"

# Capitalize the first letter of the words
capitalized = s.capitalize()

# Convert string to uppercase
uppercase = s.upper()

# Convert string to lowercase
lowercase = s.lower()

# Print the results
print(capitalized)
print(uppercase)
print(lowercase)


# Problem 4:

s = "the quick brown fox jumps over the lazy dog"

# Find the index of "fox"
index = s.find("fox")

# Count occurrences of "the"
count_of_the = s.count("the")

# Print results
print(f"index of 'fox' is {index}")
print(f"'the' {count_of_the}")


# Problem 5:

s = "I love programming in Java"
print(f"original string: {s}")

# Replace "Java" with "Python"
modified_str = s.replace("Java", "Python")

# Print the modified string
print(f"Modified string: {modified_str}")


#  Problem 6:
s = "apple,banana,cherry,dates"

# Split string into a list of substrings
substrings = s.split(',')

# Print list of substrings
print(substrings)

# Joined list of substrings into a single string with spaces
joined_string = ' '.join(substrings)

# Print joined string
print(joined_string)



