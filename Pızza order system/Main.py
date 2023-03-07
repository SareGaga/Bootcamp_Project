import csv
import datetime
from Classlar import *


def Main():
    menu = open("menu.txt", encoding="utf-8")
    print(menu.read())

    choosePizza = input("Lütfen Pizzanızı seçiniz :")
    if choosePizza == "1":
        pizza = Klasik()
    elif choosePizza == "2":
        pizza = Margherita()

    elif choosePizza == "3":
        pizza = TurkPizza()
    elif choosePizza == "4":
        pizza = DominosPizza()
    else:
        print("Geçersiz seçim")

    chooseSos = input("Lütfen pizzanız içi sos seçiniz : ")
    if chooseSos == "11":
        sos = Zeytin()
    elif chooseSos == "12":
        sos = Mantar()
    elif chooseSos == "13":
        sos = KeciPeyniri()
    elif chooseSos == "14":
        sos = Et()
    elif chooseSos == "15":
        sos = Sogan()
    elif chooseSos == "16":
        sos = Mısır()
    else:
        print("Geçersiz seçim")


    bill = pizza.get_cost() + pizza.get_cost()


    isim = input("Lütfen adınızı giriniz : ")
    tc = input("Lütfen TC giriniz : ")
    kartNo = input("Kart numaranızı giriniz : ")
    kartSifre = input("Kart şifresini giriniz\t : ")
    print("Siparişiniz alındı")

    an = datetime.datetime.now()
    date = datetime.datetime.strftime(an, " %x %X " )

    csv_file = open("Order_Database.csv", "a")
    csv_reader = csv.writer(csv_file, delimiter=",")
    csv_reader.writerow(
        [
            pizza.__class__.__name__,
            isim,
            tc,
            kartNo,
            kartSifre,
            pizza.get_description() + sos.get_description(), 
            date,
            bill,
        ]
    )


Main()
