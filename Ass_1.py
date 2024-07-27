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
