from Logic.CRUD import adauga_obiect
from Tests.test_ALL import run_all_tests
from UI.console import run_menu


def main():
    run_all_tests()
    lista = []
    lista = adauga_obiect("4", "dosar", "alb si subitre", 15.50, "AA11", lista)
    lista = adauga_obiect("2", "dosar", "alb si gros", 15.00, "AA13", lista)
    lista = adauga_obiect("3", "carte", "alba", 23.7, "AA13", lista)

    run_menu(lista)


main()
