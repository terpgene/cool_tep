#this is a test of words

word = input("What word do you want to reverse: ")
def word_submitted():
    """
    Function to accept words
    param: word = str.
    """
    
    reversed_words = word[::-1]
    print(reversed_words)

word_submitted()
    