def is_palindrome(word):
    def remove_non_alpha(string_value):
        result = ""
        for char in string_value:
            if char.isalpha():
                result += char
        return result.lower()


input_word = input("PLease enter a word: ")

