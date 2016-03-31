f = open("story.txt", 'r')
story_string = f.read()

f=open("dictionary.txt", "r")
vocabulary =f.read()

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return(story_tokens)

misspelled_words = []
clean_chars = [",", ".", "'", ";", "\n"]
tokenized_story = tokenize(story_string, clean_chars)
tokenized_vocabulary = tokenize(vocabulary, clean_chars)

for row in tokenized_story:
    if (row != "" and row not in tokenized_vocabulary):
        misspelled_words.append(row)
print("misspelled Words")
print(misspelled_words)