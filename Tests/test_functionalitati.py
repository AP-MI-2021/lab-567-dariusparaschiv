from Domanin.inventar import get_descriere
from Logic.CRUD import adauga_obiect, get_by_id
from Logic.functionalitati import concatenare


def test_concatenare():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 9.0, "AA11", lista)
    lista = adauga_obiect("2", "enciclopedie", "rosu", 39.0, "RA13", lista)

    lista = concatenare(" si mare", 10.00, lista)

    assert get_descriere(get_by_id("1", lista)) == "alb si subtire"
    assert get_descriere(get_by_id("2", lista)) == "rosu si mare"
