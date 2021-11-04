from Logic.CRUD import adauga_obiect
from Tests.test_ALL import run_all_tests
from UI.consola_noua import run_menu_nou
from UI.console import run_menu


def main():
    run_all_tests()
    lista = []
    lista = adauga_obiect("4", "dosar", "alb si subitre", 15.50, "AA11", lista)
    lista = adauga_obiect("2", "dosar", "alb si gros", 15.00, "AA13", lista)
    lista = adauga_obiect("3", "carte", "alba", 23.7, "AA13", lista)
    print("1. Meniul clasic")
    print("2. Meniu pentru apelare intr-o linie")
    while True:
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            run_menu(lista)
        elif optiune == "2":
            run_menu_nou(lista)
        elif optiune == "x":
            break
        else:
            print("optiune invalida")


main()
