from word_counter import WordFrequencyCounter 
if __name__ == "__main__":
    try:
        string = WordFrequencyCounter(1)
        print(string)
    except Exception as e:
        print(e)