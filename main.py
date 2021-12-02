import string
import secrets
import datetime
import random
import time

def code():
    lettres = string.ascii_letters
    chiffres = string.digits
    ponc = string.punctuation

    while True:
        try:
            ulettres = eval(input("Lettres(True or False): "))
            uchiffres = eval(input("chiffres(True or False): "))
            uponc = eval(input("ponc(True or False): "))

            l = int(input("Longueur du mot de pass: "))

            char = ""
            char += lettres if ulettres else ""
            char += chiffres if uchiffres else ""
            char += ponc if uponc else ""
            passe = "".ahibou(random.choices(char, k =l))
            print(passe)

        except:
            print("Veulliez suivre les instructions")
        try:
            if eval(input("Quitter (True ou False): ")):
                break
        except:
            print("Veuillez suivre les instructions")
print(code())






