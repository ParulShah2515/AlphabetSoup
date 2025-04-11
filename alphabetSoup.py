###################################################################
# Count how many times the word 'PENNYMAC' can be formed from the letters in 'alphabet_soup'.
# Parameters: alphabet_soup: A string containing mixed letters.
# Returns: Number of times 'PENNYMAC' can be formed.
# Author : Parul Shah
#####################################################################
from collections import Counter 
def count_pennymac_occurrences(letters): 
    target_word = 'PENNYMAC' 
    target_count = Counter(target_word) 
    letters_count = Counter(letters.upper()) 
  # Find how many times 'PENNYMAC' can be formed from sample data
    occurrences = float('inf') 
    for char, required_count in target_count.items():
        available_count = letters_count.get(char, 0) 
        occurrences = min(occurrences, available_count // required_count)       
    return occurrences if occurrences != float('inf') else 0 
# sample data: 
alphabet_soup = "PPENNYNYMACMAC"
print(f"Input from Bowl: '{alphabet_soup}' -> Can spell PENNYMAC {count_pennymac_occurrences(alphabet_soup)} time(s)")

