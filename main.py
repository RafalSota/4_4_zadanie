"""
>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
Podaj składnik 1. 2.3
Podaj składnik 2. 5.4
Dodaję 2.30 i 5.40
Wynik to 7.70

Sprawdzaj, czy podana wartość na pewno jest liczbą.
W wypadku mnożenia i dodawania daj użytkownikowi możliwość wpisania większej ilości argumentów 
niż tylko dwa, np. możesz dodać do siebie trzy i więcej liczb.
"""

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def calculator():
    while True:
        print("Kalkulator. Podaj działanie, posługując się odpowiednią liczbą:\n1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Dzielenie\n5. Wyjście z kalkulatora")
        operation = input("Wybór: ")
        try:
            operation = int(operation)
        except ValueError:
            logging.warning(f"WARNING Proba użycia '{operation}' jako liczby całkowitej")
        if operation == 1:
            while True:
                i = input("Ile liczb chcesz dodać? ")
                try:
                    i = int(i)
                    break
                except ValueError:
                    print("Błędna liczba. Spróbuj jeszcze raz. Podaj liczbę całkowitą ")
                    logging.warning(f"WARNING Proba użycia '{a}' jako liczby całkowitej")
            numbers = []
            result = 0
            info = ""
            for i in range(0,i):
                while True:
                    number = input(f"Podaj składnik {i+1}: ")
                    try:
                        number = float(number)
                        info += str(number) + " "
                        result += number
                        break
                    except ValueError:
                        print("Podany składnik nie jest liczbą. Spróbuj jeszcze raz.")
                        logging.warning(f"WARNING Proba użycia '{number}' jako liczby")
            print(f"Dodaję {info}")
            print(f"Wynik to: {result}\n")
            logging.info(f"INFO Wybrano dodawanie. Dodaje {info}. Wynik to: {result}\n ")
        elif operation == 2:
            while True:
                i = input("Ile liczb chcesz odejmować? ")
                try:
                    i = int(i)
                    break
                except ValueError:
                    print("Błędna liczba. Spróbuj jeszcze raz. Podaj liczbę całkowitą ")
                    logging.warning(f"WARNING Proba użycia '{a}' jako liczby całkowitej")
            numbers = []
            result = 0
            info = ""
            for i in range(0,i):
                while True:
                    number = input(f"Podaj składnik {i+1}: ")
                    try:
                        number = float(number)
                        info += str(number) + " "
                        result += number
                        break
                    except ValueError:
                        print("Podany składnik nie jest liczbą. Spróbuj jeszcze raz.")
                        logging.warning(f"WARNING Proba użycia '{number}' jako liczby")
            print(f"Odejmuję {info}")
            print(f"Wynik to: {result}\n")
            logging.info(f"INFO Wybrano odejmowanie. Odejmuję {info}. Wynik to: {result}\n ")
        elif operation == 3:
            while True:
                a = input("Podaj składnik 1: ")
                try:
                    a = float(a)
                    break
                except ValueError:
                    print("Podany składnik nie jest liczbą. Spórbuj jeszcze raz.")
                    logging.warning(f"WARNING Proba użycia '{a}' jako liczby")
            while True:
                b = input("Podaj składnik 2: ")
                try:
                    b = float(b)
                    break
                except ValueError:
                    print("Podany składnik nie jest liczbą. Spórbuj jeszcze raz.")
                    logging.warning(f"WARNING Proba użycia '{b}' jako liczby")
            result = a * b
            print(f"Mnożę {a} i {b}")
            print(f"Wynik to: {result}\n")
            logging.info(f"INFO Wybrano mnozenie. Mnoze {a} i {b}. Wynik to: {result}\n ")
        elif operation == 4:
            while True:
                a = input("Podaj składnik 1: ")
                try:
                    a = float(a)
                    break
                except ValueError:
                    print("Podany składnik nie jest liczbą. Spórbuj jeszcze raz.")
                    logging.warning(f"WARNING Proba użycia '{a}' jako liczby")
            while True:
                b = input("Podaj składnik 2: ")
                try:
                    b = float(b)
                    while b == 0:
                        print("Nie wolno dzielić przez 0!!!")
                        logging.warning(f"WARNING Proba dzielenia przez 0!")
                        b = float(input("Podaj jeszcze raz składnik 2: "))
                    break
                except ValueError:
                    print("Podany składnik nie jest liczbą. Spórbuj jeszcze raz.")
                    logging.warning(f"WARNING Proba użycia '{b}' jako liczby")
            result = a / b
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
