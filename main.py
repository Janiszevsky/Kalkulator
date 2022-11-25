import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    return x + y
  
def subtract(x, y):
    return x - y
  
def multiply(x, y):
    return x * y
  
def divide(x, y):
    return x / y
  
print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Podaj wybór(1/2/3/4): ")
  
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj składnik 1. "))
        num2 = float(input("Podaj składnik 2. "))
      
        if choice == '1':
            logging.info("Wykonuję dodawanie.")
            print("Wynik to", add(num1, num2))

        elif choice == '2':
            logging.info("Wykonuję odejmowanie.")
            print("Wynik to", subtract(num1, num2))

        elif choice == '3':
            logging.info("Wygonuję mnożenie.")
            print("Wynik to", multiply(num1, num2))

        elif choice == '4':
            logging.info("Wykonuję dzielenie.")
            print("Wynik to", divide(num1, num2))
        break
    else:
        print("Nieprawidłowe polecenie.")


