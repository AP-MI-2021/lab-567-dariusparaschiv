from Domanin.inventar import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_obiect():
    obiect = creeaza_obiect("1", "dosar", "alb si subtire", 9.0, "AA11")

    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "dosar"
    assert get_descriere(obiect) == "alb si subtire"
    assert get_pret(obiect) == 9.0
    assert get_locatie(obiect) == "AA11"
