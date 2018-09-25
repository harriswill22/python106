Word = input("Please enter a word: ")

def histogram(Word):
    new_dictionary  = {}
    for letter in Word:
        if letter in new_dictionary:
            new_dictionary[letter] = new_dictionary[letter] + 1
        else:
            new_dictionary[letter] = 1
            
    return new_dictionary

print(histogram(Word))