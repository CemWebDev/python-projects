def is_anagram(first_word, second_word):
    def remove_non_alpha(string_value):
        result = ""
        for char in string_value:
            if char.isalpha():
                result += char
        return result.lower()
    def get_char_freq(input_word):
        frequency = {}
        for char in input_word:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency
        
    cleaned_word_first = remove_non_alpha(first_word)
    cleaned_word_second = remove_non_alpha(second_word)

    first_frequency = get_char_freq(cleaned_word_first)
    second_frequency = get_char_freq(cleaned_word_second)
    
    return first_frequency == second_frequency


first_string = input("PLease enter the first word: ")
second_string = input("Please enter the second string: ")

if is_anagram(first_string, second_string):
    print(f"'{first_string}' and '{second_string}' are anagrams.")
else:
    print(f"'{first_string}' and '{second_string}' are not anagrams.")