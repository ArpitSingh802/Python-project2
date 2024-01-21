# Get input text from the user
input_text = input("Enter a text: ")


def count_words(text):
    # Split the text into words 
    words = text.split()
    
    # Count the number of words
    num_words = len(words)
    
    return num_words



# Call the function to count words
word_count = count_words(input_text)