def is_string(s):
    return len(s) == 0

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]
    
def count_vowels(s):
    vowels = 'иаоуыэяёеюИАОУЫЭЯЁУЮaeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def remove_first_occurrence(s):
    return ''.join(sorted(set(s), key=s.index))