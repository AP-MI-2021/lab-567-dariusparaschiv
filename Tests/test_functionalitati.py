
from Domanin.inventar import get_descriere, get_locatie, get_id
from Logic.CRUD import adauga_obiect, get_by_id
from Logic.functionalitati import concatenare, mutare, pret_maxim_per_locatie, ordonare_pret, afisare_suma_pret_locatie


def test_concatenare():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 9.0, "AA11", lista)
    lista = adauga_obiect("2", "enciclopedie", "rosu", 39.0, "RA13", lista)

    lista = concatenare(" si mare", 10.00, lista)

    assert get_descriere(get_by_id("1", lista)) == "alb si subtire"
    assert get_descriere(get_by_id("2", lista)) == "rosu si mare"


def test_mutare():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 9.0, "AA11", lista)
    lista = adauga_obiect("2", "enciclopedie", "rosie", 39.0, "RA13", lista)
    lista = adauga_obiect("3", "carte", "alba", 23.7, "RA13", lista)

    lista = mutare("RA13", "VVVV", lista)

    assert len(lista) == 3
    assert get_locatie(get_by_id("1", lista)) == "AA11"
    assert get_locatie(get_by_id("2", lista)) == "VVVV"
    assert get_locatie(get_by_id("3", lista)) == "VVVV"


def test_pret_maxim_per_locatie():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 9.0, "AA11", lista)
    lista = adauga_obiect("2", "enciclopedie", "rosie", 39.0, "RA13", lista)
    lista = adauga_obiect("3", "carte", "alba", 23.7, "RA13", lista)

    rezultat = pret_maxim_per_locatie(lista)

    assert rezultat["AA11"] == 9.0
    assert rezultat["RA13"] == 39.0


def test_ordonare_pret():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 29.0, "AA11", lista)
    lista = adauga_obiect("2", "enciclopedie", "rosie", 39.0, "RA13", lista)
    lista = adauga_obiect("3", "carte", "alba", 23.7, "RA13", lista)

    lista = ordonare_pret(lista)

    assert get_id(lista[0]) == "3"
    assert get_id(lista[1]) == "1"
    assert get_id(lista[2]) == "2"


def test_afisare_suma_pret_locatie():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 29.0, "AA11", lista)
    lista = adauga_obiect("2", "enciclopedie", "rosie", 30.0, "RA13", lista)
    lista = adauga_obiect("3", "carte", "alba", 20, "RA13", lista)

    rezultat = afisare_suma_pret_locatie(lista)

    assert rezultat["AA11"] == 29.0
    assert rezultat["RA13"] == 50.0
