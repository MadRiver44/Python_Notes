# Python String Method Solutions

from collections import Counter
import re

# Basic String Operations

def reverse_string(s):
    return ''.join(reversed(s))

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def first_unique_char(s):
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

def count_char(s, char):
    return sum(1 for c in s if c == char)

def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in "aeiou")

def most_frequent_char(s):
    return Counter(s).most_common(1)[0][0]

def clean_spaces(s):
    return re.sub(r'\s+', ' ', s).strip()

def trim_spaces(s):
    start, end = 0, len(s) - 1
    while start <= end and s[start] == ' ':
        start += 1
    while end >= start and s[end] == ' ':
        end -= 1
    return s[start:end+1]

def contains_all_digits(s):
    return set("0123456789").issubset(set(s))

def capitalize_words(s):
    return ' '.join(word[0].upper() + word[1:] if word else '' for word in s.split())

# Substring and Searching

def find_occurrences(s, sub):
    return [i for i in range(len(s)) if s.startswith(sub, i)]

def is_rotation(s1, s2):
    return len(s1) == len(s2) and s1 in s2 + s2

def extract_digits(s):
    return ''.join(re.findall(r'\d', s))

def longest_word(s):
    words = s.split()
    return max(words, key=len) if words else ''

def starts_and_ends_same(s):
    return len(s) > 0 and s[0] == s[-1]

# [Truncated for brevity, will include full content in final file]

