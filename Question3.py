#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.

def is_power_of_two(n):
   
    if n <= 0:
        return False
    return n & (n - 1) == 0

# Examples
numbers = [8, 6]
for num in numbers:
  if is_power_of_two(num):
    print(f"{num} is a power of two")
  else:
    print(f"{num} is not a power of two")