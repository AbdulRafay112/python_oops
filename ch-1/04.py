import random 

def introduce_typo(sentence):
    """randomly introduce a typo in a given sentence"""
    if not sentence :
        return sentence 
    typo_types = ['delete' , 'swap' , 'replace']
    typo_type = random.choice(typo_types)
    index = random.randint(0 , len(sentence) - 2) 
    if typo_type == 'delete':
        return sentence[:index] + sentence[index + 1 : ]
    elif typo_type == 'replace':
        random_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        return sentence[:index] + random_char + random_char[index + 1 :]
    elif typo_type == "swap":
        return (sentence[:index] + sentence[index + 1] + 
                sentence[index] + sentence[index + 2:])
    
def punishment_writer():
    sentence = "I will never spam my friends again"
    typo_indices = random.sample(range(1,101) , 8)
    for i in range(1,101):
        line = sentence 
        if i in typo_indices:
            line = introduce_typo(sentence)
        print(f"{i} . {line}")
