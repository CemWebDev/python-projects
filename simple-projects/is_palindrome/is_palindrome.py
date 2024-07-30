def remove_non_alpha(word):
    result = ""
    for char in word:
        if char.isalpha():
            result += char
    return result.lower()


def is_palindrome(text):
    cleaned_text = remove_non_alpha(input_word)
    return cleaned_text == cleaned_text[::-1]


input_word = input("Please enter a text: ")

if is_palindrome(input_word):
    print(f"'{input_word}' is a palindrome.")
else:
    print(f"'{input_word} is not a palindrome.")
