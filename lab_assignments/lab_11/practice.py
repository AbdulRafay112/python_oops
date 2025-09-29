import random

def my_choice(data):
    """Return a random element from non-empty sequence using randrange."""
    if len(data) == 0:
        raise ValueError("Sequence must be non-empty")
    index = random.randrange(0, len(data))  # random index select karo
    return data[index]


print(my_choice("rafay"))