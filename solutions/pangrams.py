import re

def pangrams(s):
    
    letter_set = set(re.findall('[a-z]', s.lower()))
    if len(letter_set) == 26: return "pangram"
    return "not pangram"