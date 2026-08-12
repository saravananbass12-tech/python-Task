PYTHON TASK 1: ADD TWO NUMBERS

Question:
Write a Python program to add two numbers.

Answer:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum = a + b

print("Sum:", sum)




PYTHON TASK 2: CHECK EVEN OR ODD

Question:
Write a Python program to check whether a number is even or odd.

Answer:
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")




PYTHON TASK 3: FIND THE LARGEST NUMBER

Question:
Write a Python program to find the largest of three numbers.

Answer:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)

print("Largest number:", largest)





PYTHON TASK 4: CHECK PALINDROME

Question:
Write a Python program to check whether a word is a palindrome.

Answer:
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



PYTHON TASK 5: CALCULATE FACTORIAL

Question:
Write a Python program to calculate the factorial of a number.

Answer:
number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)





