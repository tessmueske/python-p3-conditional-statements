#!/usr/bin/env python3

# Write a function admin_login() that takes two arguments, a username and a password. If the username is "admin" or "ADMIN" and the password is "12345", return "Access granted". Otherwise, return "Access denied".

def admin_login(username, password):
    if (username == 'admin' or username == "ADMIN") and password == '12345':
        return 'Access granted' 
    else:
        return 'Access denied'

# Write a function hows_the_weather() that takes in one argument, a temperature. If the temperature is below 40, return "It's brisk out there!". If the temperature is between 40 and 65, return "It's a little chilly out there!". If the temperature is above 85, return "It's too dang hot out there!". Otherwise, return "It's perfect out there!"

def hows_the_weather(temperature):
    if temperature <= 40:
        return "It's brisk out there!"
    elif temperature <= 65 and temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature >= 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

# Write a function fizzbuzz() takes in a number. For multiples of three, return "Fizz" instead of the number. For the multiples of five, return "Buzz". For numbers which are multiples of both three and five, return "FizzBuzz". For all other numbers, just return the number itself.

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# Write a function calculator() that takes three arguments: an operation and two numbers. If the operation is one of the following: +, -, *, or /, return the value of calling the operation on the two numbers. Otherwise, output a message saying "Invalid operation!" and return None.

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
        return None