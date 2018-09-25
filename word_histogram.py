Sentence = input("Please enter a sentence: ")

def histogram(Sentence):
    new_dictionary  = {}
    for word in Sentence.split():
        if word in new_dictionary:
            new_dictionary[word] = new_dictionary[word] + 1
        else:
            new_dictionary[word] = 1
            
    return new_dictionary

print(histogram(Sentence))