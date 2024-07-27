# Python Programming Assignment 01

**Implement Python programs to accomplish the following tasks**

## 1. **Age Assignments Based on the Riddle**

- **Problem Statement:** Write a program to solve this age-related riddle!
     Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
     - Anton is 21 years old.
     - Beth is 6 years older than Anton.
     - Chen is 20 years older than Beth.
     - Drew is as old as Chen's age plus Anton's age.
     - Ethan is the same age as Chen.

- Your code should store each person's age to a variable and print their names and ages at the end.
     ```python
     Anton is 3
     Beth is 4
     Chen is 5
     Drew is 6
     Ethan is 7
     ```


## 2. **Formatted String Interpolation**

   - **Task:** Given the variables `name`, `age`, and `city`, use f-strings to construct a sentence that describes a person using these variables.
     ```python
     name:str = "Alice"
     age:int = 30
     city:str = "New York"
     ```
   - **Instructions:** Use an f-string to create a sentence in the format: `"Alice is 30 years old and lives in New York."`
   - **Expected Output:**
     ```
     Alice is 30 years old and lives in New York.
     ```


    - **Task:** Given a floating-point number `value`
      - Round `value` to the nearest integer.
      - Round `value` to two decimal places.
      ```python
      value:float = 12.34567
      ```
    - **Expected Output:**
      ```
      Rounded to nearest integer: 12
      Rounded to two decimal places: 12.35