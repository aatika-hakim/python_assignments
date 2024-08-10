from typing import List

# 1. Add Two Numbers
def add_nums() -> None:
    a: int = int(input("Enter the first number: "))
    b: int = int(input("Enter the second number: "))
    total: int = a + b
    print(f"The total sum is {total}")
add_nums()

# 2. Agreement Boot
def fav_animal() -> None:
    animal: str = input("What's your favorite animal? ")
    print(f"My favorite animal is also {animal}!")
fav_animal()

# 3. Fahrenheit to Celsius
def f_to_c() -> None:
    f_temp: float = float(input("Enter temperature in Fahrenheit: "))
    c_temp: float = (f_temp - 32) * 5.0 / 9.0
    print(f"Temperature: {f_temp}F = {c_temp:.2f}C")
f_to_c()

# 4. Triangle Perimeters
def tri_perimeter() -> None:
    s1: float = float(input("Length of side 1? "))
    s2: float = float(input("Length of side 2? "))
    s3: float = float(input("Length of side 3? "))
    peri: float = s1 + s2 + s3
    print(f"The perimeter of the triangle is {peri}")
tri_perimeter()

# 5. Square Number
def square_num() -> None:
    num: float = float(input("Type a number to see its square: "))
    sq: float = num ** 2
    print(f"{num} squared is {sq}")
square_num()

# 6. Delete a Number
def del_num() -> None:
    nums: List[int] = [1, 2, 3, 4, 5]
    nums.remove(3)
    print(nums)
del_num()

# 7. Creating a List
def merge_lists() -> None:
    list1: List[int] = [1, 2, 3]
    list2: List[int] = [4, 5, 6]
    list1.extend(list2)
    print(list1)
merge_lists()

# 8. Pop Method
def pop_item() -> None:
    items: List[int] = [10, 20, 30, 40]
    removed: int = items.pop()
    print(f"Updated list: {items}")
    print(f"Removed item: {removed}")
pop_item()

# 9. Index Method
def color_index() -> None:
    colors: List[str] = ['red', 'blue', 'green', 'yellow']
    index: int = colors.index('green')
    print(f"The index of 'green' is {index}")
color_index()

# 10. Get Last Element
def last_elem(lst: List[int]) -> None:
    if lst:
        print(lst[-1])
    else:
        print("The list is empty.")
last_elem([1, 2, 3, 4, 5])  # Example list

# 11. Get a List
def user_input_list() -> None:
    lst: List[str] = []
    
    while True:
        value: str = input("Enter a value: ")
        if value == " ":
            break
        lst.append(value)
    
    print("Here's the list:", lst)
user_input_list()
