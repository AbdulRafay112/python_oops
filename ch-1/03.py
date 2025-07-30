# 📌 Question ka Matlab:
# Aapko aik program banana hai jo:

# Do amounts input le:

# Ek amount charge kiya gaya (for example: ₹73.50)

# Ek amount customer ne diya (for example: ₹100)

# Fir program ko ye calculate karna hai:

# Kitna change wapas dena hai (i.e., 100 - 73.5 = 26.5)

# Aur ye change kitne coins aur notes se dena chahiye, taake minimum number of notes/coins lagein.

from typing import Dict 
 
def make_change(amount_charge , customer_amount) -> Dict[int , int] :
    if customer_amount < amount_charge :
        raise ValueError("bhai pooray paisay do discount nhi chalega")
    change: int = customer_amount - amount_charge
    denominations = [5000 , 1000 , 500 , 100 , 50 , 20 , 10 , 5 , 2 , 1]
    change_breakdown = {}

    for denom in denominations :
        count: int = change // denom
        if count > 0:
            change_breakdown[denom] = count 
            change = change - (denom * count)
            if change == 0: 
                break
    return change_breakdown

