import random 
from typing import List , Dict 
class BirthdayParadox:
    """A class to test the birthday paradox by simulating random birthdays"""
    def __init__(self , num_simulations: int = 10000):
        """Initialize the birthday paradox tester with number of simulations
        Args:
            num_simulations: Number of simulations to run each list 
            raise ValueError if num_simulation is not a positive integer
           """
        self._validate_input(num_simulations)
        self._num_simulations = num_simulations 
        self._results: Dict[int , float] = {} # empty dict : key is number of birthdays in list , and value is the probability of each list 
    def _generate_birthdays(self , n: int) -> List[int]:
        """Generate a list of n random birthdays (1 to 365)
        Args: 
            n: number of people birthdays to generate 
            return list of random birthdays
        """
        return [random.randint(1,365) for _ in range(n)]
    def _has_same_birthdays(self , birthdays) -> bool:
        """Check if any integer is repeat on a list if an integer repeat its mean their is same birthday of atleast two people"""
        return len(birthdays) != len(set(birthdays))
    
    def run_experiments(self):
        """Run experiments for n(people) = 5 , 10 , 15 ... 100 and calcualte probabilities"""
        for n in range(5,101,5):
            success_count = 0 
            for _ in range(self._num_simulations):
                birthdays = self._generate_birthdays(n)
                if self._has_same_birthdays(birthdays):
                    success_count +=1 
            probability = success_count / self._num_simulations
            self._results[n] = probability  
    # === dunder methods ===
    def __str__(self) -> str:
        """String Representation of the experiments results"""
        header = "n\tProbability of Same Birthday\n"
        rows = [f"{n} \t {prob:.4f}" for n , prob in self._results.items()]
        return header + "\n".join(rows)

    # helper functions 
    def _validate_input(self , num_simulations: int):
        """Validate the input and raise error according to the wrong input"""
        if not isinstance(num_simulations , int):
            raise TypeError("number simulation must be integer type")
        if num_simulations <=0 :
            raise ValueError("simulation must be positive integer")
