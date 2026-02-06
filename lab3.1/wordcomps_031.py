#!/usr/bin/env python3
import sys

words = [line.strip() for line in sys.stdin if line.strip()]

seventeenLetters = [w for w in words if len(w) == 17]
eighteenmoreLetters = [w for w in words if len(w) >= 18]
containsFourA = [w for w in words if w.lower().count('a') == 4]
containstwomoreQ = [w for w in words if w.lower().count('q') >= 2]
containsCie = [w for w in words if 'cie' in w.lower()]
isAnagram = [w for w in words if sorted(w.lower()) == sorted("angle") and w.lower() != "angle"]


print(f"Words containing 17 letters: {seventeenLetters}")
print(f"Words containing 18+ letters: {eighteenmoreLetters}")
print(f"Words with 4 a's: {containsFourA}")
print(f"Words with 2+ q's: {containstwomoreQ}")
print(f"Words containing cie: {containsCie}")
print(f"Anagrams of angle: {isAnagram}")
