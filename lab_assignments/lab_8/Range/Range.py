class Range:
    """Simple Range class that mimics the behavior of built in range class of python"""
    def __init__(self , start: int , stop: int = None , step: int = 1):
        """ initialize a range
         Args: 
             start: start of the range 
             stop: stop of the range its usually stop (n-1) pattern
             step: its steps the sequence of the range 
           """
        if stop is None:# checking for 1 argument case e.g-> Range(4)
            stop = start 
            start = 0 
        self._type_validation(start , stop , step) # type validation
        self._step_validation(step) # step zero case checking 
        self._length = self._calculate_length(start , stop , step) # effective length of the range
        self._start = start 
        self._stop = stop 
        self._step = step 

    # === properties ===
    @property 
    def start(self) -> int:
        return self._start 
    @property
    def stop(self) -> int :
        return self._stop 
    @property 
    def step(self) -> int :
        return self._step 
    
    # === dunder methods ===
    def __len__(self) -> int:
        """Return number of entries in the range"""
        return self._length
    def __getitem__(self , k: int) -> int :
        k = self._negative_index_handling(k) # index negative case handling 
        self._index_validation(k)
        return self.start + k * self.step
    
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]
    def __repr__(self) -> str :
        """Developer representation"""
        return f"Range({self.start} , {self.stop} , {self.step})"
    def __str__(self) -> str :
        """client representation"""
        return f"start = {self.start} , stop = {self.stop} , step = {self.step}"
    def __eq__(self , other) -> None :
        """Compare with other Range or built in range"""
        if isinstance(other , Range) or isinstance(other , range):
            print(list(self))
            print(list(other))
            return (list(self) == list(other))
        return False 



     # === helper functions ===       
         
    def _step_validation(self , step: int)->None:
        """If step is equals to zero raise value error"""
        if step == 0:
            raise ValueError("step can not be zero")
    def _calculate_length(self , start: int , stop: int , step: int)->int:
        """Calculate the effective length of the range"""
        if (step > 0 and start >= stop) or (step < 0 and start <= stop):
            return 0
        return ((abs(stop - start) - 1) // abs(step)) + 1
        
    def _type_validation(self , start: int , stop: int , step: int) -> None :
        """Type validation of all three: start , stop , step"""
        for name , val in {"start": start , "stop": stop , "step": step}.items():
            if not isinstance(val , int):
                raise TypeError(f"{name} must be int type")
    def _negative_index_handling(self , k: int)->int:
        """if index is negative then increment to its length and return it"""
        return k + len(self) if k < 0 else k 
    def _index_validation(self , k: int) -> None:
        """Index validation and index type checking"""
        if not isinstance(k , int):
            raise TypeError("index must be int type")
        if not 0 <= k < len(self):
            raise IndexError("index out of range")

    