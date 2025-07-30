# if room contain 23 or more people 
#  to 50% ya us say zyada chanse hota hai kay kay kamz kam 2 logon ki birthday same hogi 

import random

def has_duplicate_birthdays(n):
    """Check if at least two people share the same birthday."""
    birthdays = set()
    for _ in range(n):
        birthday = random.randint(1, 365)  # Assume 365-day year
        if birthday in birthdays:
            return True
        birthdays.add(birthday)
    return False

def simulate_paradox(trials=1000):
    print("Birthday Paradox Simulation")
    print("-" * 35)
    print("People\tProbability of Shared Birthday")
    
    for n in range(5, 101, 5):
        matches = sum(has_duplicate_birthdays(n) for _ in range(trials))
        probability = matches / trials
        print(f"{n}\t{probability:.2%}")  # Show as percentage

# Run the simulation
simulate_paradox()
