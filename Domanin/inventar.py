def creeaza_obiect(id, nume, descriere, pret_achizitie, locatie):
    """
    creeaza o lista ce reprezinta un invetar
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: lista ce contine inventarul
    """
    return [id, nume, descriere, pret_achizitie, locatie]


def get_id(lst):
    """
    returneaza id-ul
    :param lst: lista care contine datele despre obiect
    :return: id-ul obiectului
    """
    return lst[0]


def get_nume(lst):
    return lst[1]


def get_descriere(lst):
    return lst[2]


def get_pret(lst):
    return lst[3]


def get_locatie(lst):
    return lst[4]
