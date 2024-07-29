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
        




first_string = input("PLease enter the first word: ")
second_string = input("Please enter the second string: ")