from Logic.CRUD import adauga_obiect, sterge_obiect
from UI.console import show_all


def command_line_console(lis, lista):
    lis_string = lis.split(";")
    try:
        for x in lis_string:
            t = x.split(",")
            if t[0] == "add":
                if len(t) != 6:
                    raise ValueError("Nu ati respectat nr de parametri")
                lista = adauga_obiect((t[1]), (t[2]), (t[3]), (t[4]), (t[5]), lista)
            if t[0] == "showall":
                show_all(lista)
            if t[0] == "delete":
                lista = sterge_obiect(t[1], lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
    return lista


def print_menu_nou():
    print("add")
    print("delete")
    print("showall")


def run_menu_nou(lista):
    print("dati comenzile separate prin: ; , iar parametrii prin: , ")
    while True:
        print_menu_nou()
        lis = input()
        lista = command_line_console(lis, lista)