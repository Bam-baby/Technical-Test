#Question 5: Reverse Integer
#Write a program that takes an integer as input and returns an integer with reversed digit ordering.

def reverse_integer(num):
  
  reversed_num = 0
  sign = 1
  # Handle negative numbers
  if num < 0:
    sign = -1
    num = abs(num)

  # Reverse digits
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

  # Apply sign back if the original number was negative
  return reversed_num * sign

# Examples
numbers = [500, -56, -90, 91]
reversed_numbers = [reverse_integer(num) for num in numbers]

print(reversed_numbers) 

# Output: [5, -65, -9, 19]
