from birthday_paradox import BirthdayParadox
if __name__ == "__main__":
    try:
        paradox = BirthdayParadox(15000)
        paradox.run_experiments()
        print(paradox)
    except Exception as e :
        print(e)