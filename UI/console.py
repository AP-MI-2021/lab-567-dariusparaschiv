from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.functionalitati import concatenare
from Domanin.inventar import get_str


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Concateneaza cuvantul citit la obiectele cu pretul mai mare decat valoarea citita")
    print("a. Afisare obiecte")
    print("x. Iesire")


def ui_adauga_obiect(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati un nume: ")
    descriere = input("Dati o descriere: ")
    pret_achizitie = input("Dati un pret: ")
    locatie = input("Dati o locatie: ")
    return adauga_obiect(id, nume, descriere, pret_achizitie, locatie, lista)


def ui_sterge_obiect(lista):
    id = input("dati id-ul obiectului pt a-l sterge ")
    return sterge_obiect(id, lista)


def ui_modifica_obiect(lista):
    id = input("Dati noul id: ")
    nume = input("Dati un nou nume: ")
    descriere = input("Dati o noua descriere: ")
    pret_achizitie = input("Dati un pret nou: ")
    locatie = input("Dati o locatie noua: ")
    return modifica_obiect(id, nume, descriere, pret_achizitie, locatie, lista)


def show_all(lista):
    for obiect in lista:
        print(get_str(obiect))


def ui_concatenare(lista):
    cuv = input("dati un string pentru a-l concatena: ")
    valoare = float(input("dati o valoare pentru comparare: "))
    return concatenare(cuv, valoare, lista)


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista)
        elif optiune == "4":
            lista = ui_concatenare(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("optiune invalida")
