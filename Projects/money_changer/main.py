from currency_system import CurrencySystem 
from change_calculator import ChangeCalculator 
from transaction import Transaction
def main():
    try:
        pkr_currency = CurrencySystem([5000 , 1000 , 500 , 100 , 50 , 20 , 10 , 5 , 2 , 1])
        transaction = Transaction(6500 , 8200)
        calculator = ChangeCalculator(transaction , pkr_currency)
        calculator.calculate_change()
        print(calculator)
    except Exception as e :
        print(e)

if __name__ == "__main__":
    main()


