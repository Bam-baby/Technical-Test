#Question 4: Capitalize Words
#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.

def capitalize_words(text):
 
  return " ".join([word.capitalize() for word in text.split()])

# Examples
text1 = "hi"
text2 = "i love programming"

capitalized_text1 = capitalize_words(text1)
capitalized_text2 = capitalize_words(text2)

print(capitalized_text1)  
print(capitalized_text2)
# Output: Hi  
# Output: I Love Programming
