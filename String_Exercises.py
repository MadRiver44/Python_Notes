# Exercise 1: Reverse a string
# Input: "Python"
# Output: "nohtyP"
def reverse_string(s):
    return s[::-1]  

# Solution
test_str = "Python"
print(reverse_string(test_str))

# Exercise 2: Count occurrences of a substring
# Input: "banana", "na"
# Output: 2
def count_substring(s, sub):
    return s.count(sub)

# Solution
test_str = "banana"
test_sub = "na"
print(count_substring(test_str, test_sub))

# Exercise 3: Check if a string is a palindrome
# Input: "racecar"
# Output: True
def is_palindrome(s):
    return s == s[::-1]

# Solution
test_str = "racecar"
print(is_palindrome(test_str))

# Exercise 4: Remove vowels from a string
# Input: "hello world"
# Output: "hll wrld"
def remove_vowels(s):
    return ''.join([char for char in s if char.lower() not in 'aeiou'])

# Solution
test_str = "hello world"
print(remove_vowels(test_str))

# Exercise 5: Replace multiple spaces with a single space
# Input: "This  is   a    test"
# Output: "This is a test"
import re
def normalize_spaces(s):
    return re.sub(r'\s+', ' ', s).strip()

# Solution
test_str = "This  is   a    test"
print(normalize_spaces(test_str))

# Exercise 6: Extract digits from a string
# Input: "abc123xyz456"
# Output: "123456"
def extract_digits(s):
    return ''.join(filter(str.isdigit, s))

# Solution
test_str = "abc123xyz456"
print(extract_digits(test_str))

# Exercise 7: Capitalize first letter of each word
# Input: "hello world! python is great."
# Output: "Hello World! Python Is Great."
def capitalize_words(s):
    return s.title()

# Solution
test_str = "hello world! python is great."
print(capitalize_words(test_str))

# More exercises will follow...
