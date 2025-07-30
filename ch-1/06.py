# P-1.36 Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You
# need not worry about efficiency at this point, however, as this topic is
# something that will be addressed later in this book.

def words_count():
    user_input = input("Enter words seperated by spaces ")
    words = user_input.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1 
        else:
            word_count[word] = 1 
    print("\n checking frequencies of word")
    for word , count in word_count.items():
        print(f"{word} : {count}")
words_count()