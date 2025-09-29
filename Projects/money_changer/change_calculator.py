class ChangeCalculator:
    """this class calculates change in minimum number of notes / coins"""
    def __init__(self , transaction , currency_system):
        self.transaction = transaction  # composition 
        self.currency_system = currency_system # composition 
        self.result = {}
    def calculate_change(self):
        """set result dictionary as {denomination : count}"""
        change = self.transaction.get_change()
        denomination = self.currency_system.denominations # using getters 
        for denom in denomination:
            if change == 0 : # if change becomes zero skip remainig iterations
                break 
            count , change = divmod(change , denom) # return quotient and remainder in terms of tuple
            if count > 0 :
                self.result[denom] = count 

    def __str__(self):
        if not self.result:
            return "No Change Required"
        lines = ["Change Breakdown: "]
        for denom , count in self.result.items():
            lines.append(f" {denom} x {count}")
        return "\n".join(lines)

    



    
