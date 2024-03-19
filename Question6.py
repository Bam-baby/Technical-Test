#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.

def count_vowels(sentence):
  
  vowels = "aeiou"  
  count = 0
  # Convert sentence to lowercase
  sentence_lower = sentence.lower()
  for char in sentence_lower:
    if char in vowels:
      count += 1
  return count

# Example sentence
sentence = "Hello, world!"
vowel_count = count_vowels(sentence)
print(f"The sentence '{sentence}' has {vowel_count} vowels.")

# Output: The sentence 'Hello, world!' has 2 vowels.