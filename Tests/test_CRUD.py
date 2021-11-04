from Domanin.inventar import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_obiect, get_by_id, sterge_obiect, modifica_obiect


def test_adauga_obiect():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 5.50, "AA11", lista)

    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "dosar"
    assert get_descriere(get_by_id("1", lista)) == "alb si subtire"
    assert get_pret(get_by_id("1", lista)) == 5.50
    assert get_locatie(get_by_id("1", lista)) == "AA11"


def test_sterge_obiect():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 5.50, "AA11", lista)
    lista = adauga_obiect("2", "plic", "negru", 2.50, "BA12", lista)
    lista = sterge_obiect("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None

    try:
        lista = sterge_obiect("4", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert get_by_id("2", lista) is not None


def test_modifica_obiect():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 5.50, "AA11", lista)
    lista = adauga_obiect("2", "plic", "negru", 2.50, "BA12", lista)
    lista = modifica_obiect("1", "dosar", "alb", 5.50, "AA11", lista)

    obiect_nou = get_by_id("1", lista)

    assert get_id(obiect_nou) == "1"
    assert get_nume(obiect_nou) == "dosar"
    assert get_descriere(obiect_nou) == "alb"
    assert get_pret(obiect_nou) == 5.50
    assert get_locatie(obiect_nou) == "AA11"

    obiect_neupdatat = get_by_id("2", lista)

    assert get_id(obiect_neupdatat) == "2"
    assert get_nume(obiect_neupdatat) == "plic"
    assert get_descriere(obiect_neupdatat) == "negru"
    assert get_pret(obiect_neupdatat) == 2.50
    assert get_locatie(obiect_neupdatat) == "BA12"

    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 5.50, "AA11", lista)

    obiect_neupdatat = get_by_id("1", lista)
    assert get_id(obiect_neupdatat) == "1"
    assert get_nume(obiect_neupdatat) == "dosar"
    assert get_descriere(obiect_neupdatat) == "alb si subtire"
    assert get_pret(obiect_neupdatat) == 5.50
    assert get_locatie(obiect_neupdatat) == "AA11"


def test_get_by_id():
    lista = []
    lista = adauga_obiect("1", "dosar", "alb si subtire", 5.50, "AA11", lista)
    lista = adauga_obiect("2", "plic", "negru", 2.50, "BA12", lista)

    assert get_by_id("1", lista) == ["1", "dosar", "alb si subtire", 5.50, "AA11"]
    try:
        adauga_obiect("4", "plic", "verde", 22.50, "BA12", lista)
    except ValueError:
        assert get_by_id("3", lista) is None
        assert get_by_id("4", lista) is not None
