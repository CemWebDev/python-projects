def word_counter(text):
    text = text.lower()
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    
    words = text.split()
    
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

text_input = input("Please enter a text: ")

cleaned_text = word_counter(text_input)

for word, count in cleaned_text.items():
    print(f"'{word}': {count} times")