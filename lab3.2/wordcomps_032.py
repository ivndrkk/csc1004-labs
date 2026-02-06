#!/usr/bin/env python3
import sys

words = [line.strip() for line in sys.stdin]
words_lower = [word.lower() for word in words]

vowels = set('aeiou')
words_with_all_vowels = [word for word in words_lower if all(vowel in word for vowel in vowels)]
shortest = min(words_with_all_vowels, key=len)
original_shortest = [word for word in words if word.lower() == shortest][0]
print(f"Shortest word containing all vowels: {original_shortest}")

iary_count = len([word for word in words_lower if word.endswith('iary')])
print(f"Words ending in iary: {iary_count}")

e_counts = [(word, words_lower[i].count('e')) for i, word in enumerate(words)]
max_e_count = max(e_counts, key=lambda x: x[1])[1]
words_with_most_e = [word for word, count in e_counts if count == max_e_count]
print(f"Words with most e's: {words_with_most_e}")
