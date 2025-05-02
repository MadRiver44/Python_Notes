#!/usr/bin/env
# Imports
import re
from collections import Counter
# Generate Docstring Shortcut cmd shift 2

# Basic String Operations

# 1. Reverse a string with and without slicing
def reverse_str(s):
    """
    Reverse a string with slicing
    Args:
        s (String): string of length n
    """
    return s[::-1]

def reverse_str_no_slice(s):
    """
    Reverse a string without slicing
    Args:
        s (String): string of length n
        * reversed() returns an iterator object that accesses the sequence in reverse
        * the empty string is the wrapper for the reversed result after join()
        * join() take the iterable and joins them into one string
    """    
    new_str = "".join(reversed(s))
    return new_str

# 2. Check if two Strings are anagrams
def anagram_check(s1, s2):
    """
    check if two strings are anagrams
    Args:
        s1 (_string_): a string of lenth n
        s2 (_string_): a string of lenth n
    """   
    # check if the length of each matches, then if all the letters match
    if len(s1) == len(s2):
        return sorted(s1) == sorted(s2)
    else:
        return False 
    
# 3. Find the first non-repeating character in a string
def non_repeating_char(s):
    """
    find the first non repeating character in a string
    Args:
        s (string): string of length n
    """  
    # using DICT COMPREHENSION is quadratic, once to loop over the string and create the set, and again 
    # for each each unique letter to count the number of times it appears, traverses 1 + n times
    # items = {char: s.count(char) for char in set(s)}
    
    # use a Counter from collections lib , https://docs.python.org/3/library/collections.html
    
    # Counter from collections lib, creates a dict with the elements as a key and the count as value
    # Counters are similar to Bags as a data structure in other languages.
    # Here, we create the dict from s, and loop over the dict and check for a key with a value of only 1
    
    count = Counter(s) # this returns a dictionary of the count of occurances of the items in the collection
    for char in s:
        if count[char] == 1:    # this is where we detect the only char with count 1  
            return char
    return None     # is there are no non repeating chars, returns None
    
# 4. Count all occurances of a character in a string WITHOUT using count()  
def num_of_occurances(s):
    """
    Count all occurances of characters in a string, without using count()
    Args:
        s (string): a string of length n
    Returns:
        dict: a hash table with chars as key, and count as values
    """
    # Created a dict, then looped over the string and if the string is already in the table, increment the value by 1,
    # else, if the key is not in the dict, set the value to 1.
    
    ## Alternatively:
    #! return sum(1 for c in s if c == char)
    #? use a list comprehension and find the char that was passed as an arg
    #? if it matches, add 1 to the sum
    
    table = {}
    for char in s:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
    return table
            
# 4a. Count all occurances of a character in a string, without using count
def x_occurances(str, char):
    """
    Count the total number of occurances of a character in a string

    Args:
        letter (string): character to count
        str (string): string to search
    """
    count = 0    
    for item in str:
        if item == char:
            count += 1
    return (char, count)

# 5. Remove all vowels from a string
def remove_vowels(str):
    """
    Remove all vowels from a string
    Args:
        str (string): string to search through
    """    
    # the list comprhension is passed in as an arg to .join()
    # .join() is a string method that concatenates the result of the iterable
    # the '' before .join is the empty string providing the method which acts as the seperator
    # in other words there will be no space when the vowel is filtered out
    vowels = 'AEIOUaeiou'
    return ''.join(char for char in str if char not in vowels)

# 6. Find the most frequent character in a string 
def most_freq_char(str):
    """
    Find the most frequent character in a string
    Args:
        str (string): string of length n
    """ 
    # first we create a hash table of characters and counts
    # we then take the table and convert it to a list of tuples using .items()
    # we get a dict_items(), where we can only use .sorted on that list
    # to sort the list of tuples, we pass a lambda function and use another param, reverse=True
    # to sort descending.
    
    # when you want to sort a list of tuples by a particular element, use a lambda function
    # with lambda as the key. A function must be defined inside the key param which helps the 
    # sort funtion identify which index to choose.
    
    # ! Todo Time complexity of this
    # Alternatively:
    # Use most_common() method from Counter to get the ordered list of most common items,
    # from most common to least and extract their element and count from the tuple
    # The sorted list of tuples in my answer is what the above does more succinctly
    #! return Counter(s).most_common(1)[0][0]
    
    table = {}   
    for char in str:
        if char in table:
            table[char] = table[char] + 1
        else:
            table[char] = 0
    list_of_tuples = table.items()
    return sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    
    
# 7. Replace multiple spaces in a string with a single space
def replace_spaces(s):
    """
    Replace multiple spaces in string with a single space
    Args:
        s (string): a string of length n
    """        
    # u+0020 unicode for whitespace
    # I want to use a REGEX for this, https://docs.python.org/3/library/re.html
    # REGEX How To: https://docs.python.org/3/howto/regex.html#regex-howto
    # REGEX's must first be compiled, re.compile(regex passed in as a string!). They are passed in as strings because
    # regular expressions are not part of the core Python language
    # 

    return re.sub(r'\s+', " ", s).strip()

# 8. Implement a function that trims leading and trailing spaces (without using `strip()`).
def trim_lead_and_trailing(s):
    """_summary_
    Implement a function that trims leading and trailing spaces (without using `strip()`).
    Args:
        s (string): string of length n

    Returns:
        _type_: copy of string without leading or trailing whitespaces
    """
    # Turn the string into a list, remove first and last indices, then join the list back to string
    elements = s.split(" ")
    del elements[0]
    del elements[-1]
    return " ".join(elements)

    # Alternatively, use slicing by setting the starting and ending indices
    """ 
    start, end = 0, len(s) - 1
    while start <= end and s[start] == ' ':
        start += 1
    while end >= start and s[end] == ' ':
        end -= 1
    return s[start:end+1]
    """

# 9. Check if a string contains all the digits from 0 to 9.
def contains_digits(s):
    # This gets all the numbers, but not if all nums 0-9 are present
    return re.findall(r'[0-9]', s)

def contains_all_digits(s):
   # Use the set data structure of non duplicated elements, then set if all of those elements
   # appear in the other. .issubset() - Tests if every member is in the passed in arg
   return set('0123456789').issubset(s)
      
    
# 10. Capitalize the first letter of every word without using `title()`.  
import string
def first_letter_caps(s):
    """
    Capitalize the first letter of every word without using `title()`.

    Args:
        s (string): return a string with each word capitalized
    """
    # split capitalize join
    elements = s.split() # split the string into pieces
    new_list = [item.capitalize() for item in elements] # iterate over the list and capitalize each element
    return " ".join(new_list)

    # Alternatively:    
    # return string.capwords(s)
    
#  Substring and Searching

# 11. Find all occurrences of a substring in a string.
def all_occurances(sub, s):
    """
    find all occurances of a substring in a string
    Args:
        sub (string): substring pattern to search for
        s (string): string to search through
    """
    # A. str.find() - returns the lowest index in the string where the substring is found between slice options
    # https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring?page=1&tab=modifieddesc#tab-top
    index = s.find(sub) # find the first occurance
    while index != -1: # as long as index remains positive, continue to loop
        yield index # yield means we are creating a generator
        index = s.find(sub, index + 1)
    # below returns a generator object, to see it we must make it a list or a string
    # this does not go in the function
    [(index, s[index: index + 2]) for index in all_occurances('na', 'banananandndnannddjfsdkifdana')]
    
    # Prettiest solution. Note that one can easily generalize by introducing optional parameter 
    # overlapping=True and replacing i+1 by i + (1 if overlapping else len(p)).
    
    # B. Regex
    # [m.start() for m in .finditer('test', 'test test test test')]
    # overlapping with look ahead
    # [m.start() for m in re.finditer('(?=tt)', 'ttt')]
    
# 12. Check if a string is a rotation of another string.
def string_rotation(s1_origin, s2_rotation):
    # we concatenate the origin string and see if the rotation is contained within
    # return len(s1_origin) == len(s2_rotation) and s2_rotation in s1_origin + s1_origin

    if len(s1_origin) != len(s2_rotation):
        return False
    if len(s1_origin) == 0:
        return True  # Empty strings are rotations of each other
    return s2_rotation in s1_origin + s1_origin
        
        
# 13. Extract all numeric digits from a string.
def extract_nums(s):
    # extract the nums and return the string
    regex = re.compile('\d')
    return regex.findall(s) # found all the digits, returns a list
    # return ''.join(regex.findall(s)) # returns a string
    # or
    # return ''.join(re.findall(r'\d', s))     
        

    
# 14. Find the longest word in a string.
def longest_word_in_string(s):
    words = s.split()    # break into a list
    return sorted([word for word in words], key=len, reverse=True)[0] # use sorted on  the list with key=len and reverse=True
        

# 15. Check if a string starts and ends with the same character.
def same_char(letter, s):
    if len(s) > 0 and s[0] == letter and s[-1] == letter:
        return True
    return False


# 16. Find the position of the second occurrence of a substring.
def second_occurance(sub, s): # 'abcdsdkdjfabcuieeupr'
    pattern = re.compile('abc')
    arr = pattern.findall(s)
    if len(arr) > 0:
        return arr[1]
    return -1

# or use str.find(),

# get first occurance
# then increment that first occurance to get the second
# return s.find(sub, first + 1) if first != -1 else -1
    
# 17. Find all words starting with a given letter in a sentence.
def find_starting_letter(letter, s):
    results = []
    arr = s.split()
    for item in arr:
        if item[0] == letter:
            results.append(item)
    return results

# or
# loop over the list created from sentence.split(), then
# lowercase the whole word and see if it starts with the letter in lowercase also1
# return [word for word in sentence.split() if word.lower().startswith(letter.lower())]


# 18. Extract the domain name from an email address.
def domain(s):
    start = s.find('@')
    if start == -1:
        return False
    return s[start+1:]

# 19. Check if one string can be formed by reordering another (permutation check).
# Poorly written, come back later
# def string_reorder(s1, s2):
    

# 20. Find the longest common prefix among a list of strings. 

def common_prefix(arr):
    # sorted_copy = sorted([item for item in arr], key=len, reverse=True)
    # last_item = sorted_copy[-1]
    # middle_index = len(last_item) / 2
    # last_item_prefix = last_item[:2]
    # for prefix in sorted_copy:
    #     if prefix[:2] == last_item_prefix:
    if not arr: return ""
    prefix = arr[0]
    for s in arr[1:]:
        print(s)
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            print(prefix)
            if not prefix:
                return ""
    return prefix


## String Formatting & Cleaning

# 21. Convert a string into a valid variable name (only alphanumeric and underscores).

# no reserved words, can't start with a num, no hyphens,
# My solution seems to work as compared to the exercise solution
def convert_to_variable(s):
    copy = s.split("_")
    print(copy)
    reservered_words = ['if', 'else', 'def', 'elif', 'while', 'return', 'print', 'for']
    starts_with = [0,1,2,3,4,5,6,7,8,9, '-']
    for char in copy:
        print(char)
        if copy in reservered_words or s.startswith(char) and not s.startswith('_'):
            return False
    return True


# 22. Convert a camelCase string to snake_case

def convert_camel_case(s):
# don't understand the first part of the regex
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
    
    
    
# 23. Format a number in a string with commas as a thousand separator.

#  format examples https://docs.python.org/3/library/string.html#format-examples
def number_format(num_str):
    return "{:,}".format(int(num_str))


# 24. Check if a string follows the format of a valid IPv4 address.

# 192.168.1.1 example
def valid_ipv4_format(ip):
    # split into parts
    # there are 4 parts to the ip, they are all digits, the range is 0 - 255
    parts = ip.split('.')
    return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
    


# 25. Remove duplicate words from a sentence.
def remove_dupes(str):
    # solution, but does not preserve the order of the sentence
    # items = set(str.split())
    # return " ".join(items)

    # much better
    unique = set()
    results = []
    items = str.split()
    for word in items:
        if word not in unique:
            unique.add(word)
            results.append(word)
    return " ".join(results)

# 26. Pad a string with leading zeros to make it a fixed width.

def string_padding(s, width):
    string_len = len(s)
    if string_len > width:
        return s
    else:
        padding_size = width - string_len
        num_of_zeros =  str(0) * padding_size
        return num_of_zeros + s
    
    # there is a fucking built in for this?!!!
    # return s.zfill(width)
        

# 27. Replace all punctuations with a space.
    #regex replace
    
def replace_punctuation(s):
    # mine
    return re.sub(r'[!.,;]', "", s)
    # solution ans
    # regex = replace any non alphanumeric and whitespace 
    # return re.sub(r'[^\w\s]', "", s)
    
    
# 28. Convert a list of words into a single hyphen-separated string.
def add_hyphens(str):
    return "-".join(str)

# 29. Remove a given word from a string.
def remove_word(word, str):
    start = str.find(word)
    end = start + len(word)
    return str.replace(str[start:end+1], '')

# 30. Convert an integer to a binary string without using `bin()`.
# divide int % 2 get remainder
# get the integer quotient for the next iteration  int // 2 (floor division with no decimal)
# continue till quotient is zero

def convert_to_binary(num): 
    if num == 0: return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary


## Advanced String Transformations
# 31. Convert a string of comma-separated numbers into a list of integers.

# split the list with comma delimeter
# loop and convert each item to an int in a new list

def csv_list(s):
    new_list = s.split(',')
    return [int(item) for item in new_list]

    return [int(num) for num in s.split(',') if num.strip().isdigit()]


# 32. Convert a string to Pig Latin (move the first letter to the end and add "ay").

def pig_latin(s):
    first_letter = s[:1]
    return  s[1:] + first_letter + 'ay'
    
 
# 33. Implement a basic version of `str.join()` for a list of strings.

def str_join(arr):
    # works, but need seperator as in the docs
    items = ''
    for item in arr:
        items += item 
    return items

    # solution
    # result = ""
    # for i, item in enumerate(lst):
    #     result += item
    #     if i < len(lst) - 1:
    #         result += sep
    # return result


# 34. Count the number of palindromic substrings in a given string.

#def palindrome_sub(s):
    
    
    
# 35. Find the longest substring without repeating characters.
# 36. Check if a string is a valid palindrome after removing non-alphanumeric characters.

def is_palindrome(s):
    s = "".join(letter.lower() for letter in s if letter.isalnum())
    return s == s[::-1]
    
# 37. Implement a simple run-length encoding for a string.
# 38. Expand a string with abbreviations like "a2b3" into "aabbb".

def expand_abbr(s):
    results = ''
    length = len(s)
    index = 0
    while index < length:
        if index < length -1 and s[index+1].isdigit():
            results += s[index] * int(s[index+1])
            index += 2
        else:
            results += s[index]
            index += 1
    return results
            

# 39. Implement a function that extracts hashtags from a tweet.

def extract_hashtag(s):
    return re.findall(r'#\w+', s)
    
        
# 40. Convert a given string to Leetspeak (e.g., replace "e" with "3", "a" with "4", etc.).

def leetspeak(s):
    '''
    The str, string built in type has a maketrans() method to create a mapping.
    You pass strings of equal length, first arg are the characters to be mapped to, the second arg are the
    new characters, each mapped to the position of the characters of the first arg, position by position.
    After creating this mapping, use .translate() and pass the mapping that is held in a varaiable.
    '''
    mapping = str.maketrans("aeiost", "43105+")
    return s.translate(mapping)
    
## Miscellaneous String Challenges
# 41. Convert a given number to its Roman numeral representation.

def roman_numerals(num):
    # range is a built in type of immutable sequences of numbers.
    # it is used to loop a specific number of times in a for loop
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    romans = ''
    for i in range(len(numbers)): # we are looping over a range of numbers up to length of numbers list (13)
        while num >= numbers[i]: # while num passed in is greater than the number at a looped position, 
            romans =+ symbols[i] # we will increment the empty string with the symbol
            num -= numbers[i] # then we reduce the num by the number at that position and loop again with the rest of the number
    return romans
            
        
# 42. Find the longest palindromic substring in a given string.

def longest_palindrome(s):
    
    
# 43. Check if a given string is a valid email address.
# 44. Implement a function to find the edit distance between two strings.
# 45. Write a function to determine if a string follows a given regex pattern.
# 46. Convert a string with Unicode characters to ASCII equivalents.
# 47. Split a string into chunks of a given size.
# 48. Sort words in a sentence by length.
# 49. Convert an English phrase into Morse code.
# 50. Determine if two strings are one edit away from each other (insert, delete, replace one character).



if __name__ == '__main__':
    # print(reverse_str('hello'))
    # print(reverse_str_no_slice('score'))
    # print(anagram_check('holy moly', 'moly hloy'))
    # print(non_repeating_char('aadddbbbcccxeeennn'))
    # print(num_of_occurances('alsjfkljfdjdkldjsfl;adhfdhdif'))
    # print(x_occurances('holllly moly, Batman!', 'l'))
    # print(remove_vowels('there was a dog who had name and his name wa bingo'))
    # print(most_freq_char('ooohhh babababdkdododododod the bird is the word'))
    # print(replace_spaces('  the  quick brown fox  jumped  over the lazy  dog  '))
    # print(trim_lead_and_trailing(' the quick brown fox '))
    # print(contains_digits('dlksjflskdj9093 wrerjj  e93r'))
    # print(first_letter_caps('the quick black fox jumped over the lazy riley'))
    # print(all_occurances('na', 'banananandndnannddjfsdkifdana'))
    # print(string_rotation("waterbottle", "erbottlewat"))
    # print(extract_nums('jdf;alksjf;l1,1329483974,,,433423isdjlf38'))
    # print(longest_word_in_string('a dog sometimes gets sunshine on his ass'))
    # print(same_char('s', 'sunshines'))
    # print(second_occurance('abc','abcdsdkdjfabcuieeupr'))
    # print(find_starting_letter('s', 'she sells toenails by the seashore' ))
    # print(domain('kevin@gmail.com'))
    # print(common_prefix(["flower","flow","flight"]))
    # print(remove_dupes('the fox went with the fox to hunt a fox'))
    # print(add_hyphens(['the', 'fox', 'went', 'to', 'hunt', 'a', 'foxy', 'fox']))
    # print(remove_word('trump', 'this motherfucker trump needs to fucking go'))
    # print(convert_to_variable("2_fora_variable"))
    # print(convert_camel_case('camelCaseSnake'))
    # print(number_format('10231094'))
    # print(valid_ipv4_format('191.234.1.10'))
    # print(string_padding('access', 13))
    # print(replace_punctuation('the crazy; fox!'))
    # print(convert_to_binary(44535))
    # print(csv_list('1,2,3,4,5,6'))
    print(pig_latin('victory'))
    print(str_join(['a', 'b', 'c', 'd']))
    print(expand_abbr('a3b4c5'))