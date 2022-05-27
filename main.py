# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True




first_word = input("Enter your first word or sentence: ")
second_word = input("Enter your second word or sentence: ")
def find_anagram(first_word, second_word):
    if len(first_word) == len(second_word) and sorted(first_word) == sorted(second_word):
        return True
    else:
        return False


print(find_anagram(first_word,second_word))



 
