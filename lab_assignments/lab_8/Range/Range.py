class Range:
    """Our Own Range class that mimics range in python
    Our Range class is different in two ways from python range class 
    1- it has a default constructor means if you donot provide any argument its ok for Range
    2- it has copy constructor logic 
    """
    def __init__(self , start = 0 , stop = None , step = 1): # default constructor
        """Initialize the Range class constructor
        Args:
            start : integer you wants to start the sequence 
            stop: integer you wants to end the sequence but it always ends number-1
            step: integer you want to step your sequence 
        """
        if isinstance(start , Range) :
            # copy constructor logic
            self._length = start._length
            self._start = start._start 
            self._step = start._step 
            self._stop = start._stop 
        else:
            self._step_validation(step)
            self._type_validation(step)
            self._type_validation(start)
            if stop is not None :
                self._type_validation(stop)
            if stop is None :
                # handling one argument case 
                stop = start 
                start = 0 
            # protected instance variables 
            self._length = self._calculate_length(start , stop , step)
            self._start = start 
            self._step = step 
            self._stop = stop     

    # === dunder methods === 
    def __len__(self):
        """Return length of the range"""
        return self._length
    def __getitem__(self , j):
        """Return entry at index k use standar interpretation if j < 0 which support negative indexing"""
        self._validate_index(j)
        if j<0:
            j+=len(self)
        return self._start + j * self._step 
    def __str__(self):
        """String representation of range"""
        return f"start is {self._start} , stop is {self._stop} , step is {self._step}"

    # === helper methods ===

    def _validate_index(self , j):
        if j >= len(self):
            raise IndexError("index is exceed")
        if not isinstance(j , int):
            raise TypeError("index should be int type")
        
    @staticmethod
    def _step_validation(step):
        if step == 0:
            raise ValueError("step can not be zero")
    @staticmethod
    def _type_validation(other):
        if not isinstance(other , int):
            raise TypeError("Start , stop , step must be integer type")
    @staticmethod
    def _calculate_length(start , stop , step):
        """Calculate length of the range"""
        return max(0, (stop - start + step - 1) // step)


