"""
>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
Podaj składnik 1. 2.3
Podaj składnik 2. 5.4
Dodaję 2.30 i 5.40
Wynik to 7.70
"""

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def calculator():
    while True:
        print("Kalkulator. Podaj działanie, posługując się odpowiednią liczbą:\n1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Dzielenie\n5. Wyjście z kalkulatora")
        operation = int(input("Wybór: "))

        if operation == 1:
            a = int(input("Podaj składnik 1: "))
            b = int(input("Podaj składnik 2: "))
            result = a + b
            print(f"Dodaję {a} i {b}")
            print(f"Wynik to: {result}\n")
            logging.info(f"INFO Wybrano dodawanie. Dodaje {a} i {b}. Wynik to: {result}\n ")
        elif operation == 2:
            a = int(input("Podaj składnik 1: "))
            b = int(input("Podaj składnik 2: "))
            result = a - b
            print(f"Odejmuję {a} i {b}")
            print(f"Wynik to: {result}\n")
            logging.info(f"INFO Wybrano odejmowanie. Odejmuje {a} i {b}. Wynik to: {result}\n ")
        elif operation == 3:
            a = int(input("Podaj składnik 1: "))
            b = int(input("Podaj składnik 2: "))
            result = a * b
            print(f"Mnożę {a} i {b}")
            print(f"Wynik to: {result}\n")
            logging.info(f"INFO Wybrano mnożenie. Mnoze {a} i {b}. Wynik to: {result}\n ")
        elif operation == 4:
            a = int(input("Podaj składnik 1:: "))
            b = int(input("Podaj składnik 2: "))
            while b == 0:
                print("Nie wolno dzielić przez 0!!!")
                logging.warning(f"WARNING Proba dzielenia przez 0!")
                b = int(input("Podaj jeszcze raz składnik 2: "))
            result = round((a / b),12)
            print(f"Dzielę {a} i {b}")
            print(f"Wynik to: {result}\n")
            logging.info(f"INFO Wybrano dzielenie. Dziele {a} i {b}. Wynik to: {result}\n ")
        elif operation == 5:
            logging.info("INFO Wybrano wyjscie z kalkulatora")
            print("\nDziękujemy za skorzystanie z kalkulatora. Zapraszamy ponownie :)\n")
            exit()
        else:
            print("Zły wybór. Spróbuj jeszcze raz.\n")

if __name__ == "__main__":
    calculator()
