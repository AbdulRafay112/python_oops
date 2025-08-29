import string 

class WordFrequencyCounter:
    """Class that counts Words Frequencies in a string"""
    def __init__(self , input_string: str):
        """Initialize the constructor with input string which is later separated by white spaces in the form of list so we can iterate over it """
        self._input_validator(input_string)
        self.input_string = self._clean_text(input_string) # clean text with clean text method 
        self._frequency = {} # empty dict for counts of words 

    @property 
    def frequency(self):
        if self._frequency :
            return self._frequency
        else:
            self.count_words() 
            return self._frequency

    def count_words(self):
        """Count the Words in a string seperated by white spaces"""
        words = self.input_string.split() # split on white spaces 
        for word in words :
            if word in self._frequency:
                self._frequency[word] += 1 
            else:
                self._frequency[word] = 1 
    # === magic methods ===
    def __str__(self) -> str :
        """Return the string representation"""
        return "\n".join(f"{word}:{count}" for word , count in self.frequency.items()) # comprehension way

    # helper functions
    def _input_validator(self , input_string: str):
        if not isinstance(input_string , str):
            raise TypeError("Input must be string Type")
    def _clean_text(self , text: str) -> str:
        """Return the copy of cleaned string"""
        return text.lower().translate(str.maketrans("" , "" , string.punctuation))
    


