from Logic.CRUD import adauga_obiect, sterge_obiect, modifica_obiect
from Logic.functionalitati import concatenare, mutare, pret_maxim_per_locatie, ordonare_pret, afisare_suma_pret_locatie
from Domanin.inventar import get_str


def print_menu():
    print("1. Adaugare obiect")
    print("2. Stergere obiect")
    print("3. Modificare obiect")
    print("4. Concateneaza cuvantul citit la obiectele cu pretul mai mare decat valoarea citita")
    print("5. Mutare obiect din locatia initiala in locatia finala")
    print("6. Determinare cel mai mare pret pentru fiecare locatie")
    print("7. Ordonare a obiectelor crescator dupa pretul de achizite")
    print("8. Afisare sumelor preturilor pt fiecare locatie")
    print("a. Afisare obiecte")
    print("u. Undo")
    print("x. Iesire")


def ui_adauga_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati un nume: ")
        descriere = input("Dati o descriere: ")
        pret_achizitie = input("Dati un pret: ")
        locatie = input("Dati o locatie: ")
        rezultat = adauga_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_obiect(lista, undo_list, redo_list):
    try:
        id = input("dati id-ul obiectului pt a-l sterge ")
        rezultat = sterge_obiect(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_obiect(lista, undo_list, redo_list):
    try:
        id = input("Dati noul id: ")
        nume = input("Dati un nou nume: ")
        descriere = input("Dati o noua descriere: ")
        pret_achizitie = input("Dati un pret nou: ")
        locatie = input("Dati o locatie noua: ")
        rezultat = modifica_obiect(id, nume, descriere, pret_achizitie, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for obiect in lista:
        print(get_str(obiect))


def ui_concatenare(lista, undo_list, redo_list):
    try:
        cuv = input("dati un string pentru a-l concatena: ")
        valoare = float(input("dati o valoare pentru comparare: "))
        rezultat = concatenare(cuv, valoare, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_mutare(lista, undo_list, redo_list):
    try:
        locatie_initiala = input("dati o locatie din care sa se mute obiectele: ")
        locatie_finala = input("dati o locatie in care sa se mute obiectele: ")
        rezultat = mutare(locatie_initiala, locatie_finala, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_pret_maxim_per_locatie(lista):
    rezultat = pret_maxim_per_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {}".format(locatie, rezultat[locatie]))


def ui_ordonare_pret(lista, undo_list, redo_list):
    undo_list.append(lista)
    redo_list.clear()
    show_all(ordonare_pret(lista))


def ui_afisare_suma_pret_locatie(lista):
    rezultat = afisare_suma_pret_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_concatenare(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_mutare(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_pret_maxim_per_locatie(lista)
        elif optiune == "7":
            ui_ordonare_pret(lista, undo_list, redo_list)
        elif optiune == "8":
            ui_afisare_suma_pret_locatie(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "x":
            break
        else:
            print("optiune invalida")
