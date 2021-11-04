from Domanin.inventar import creeaza_obiect, get_id


def adauga_obiect(id, nume, descriere, pret_achizitie, locatie, lista):
    """
    adauga un obiect intr o lista
    :param lista: lista cu obiecte
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: o lista care contine obiectele vechi si obiectul nou
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    if type(pret_achizitie) != float:
        raise ValueError("Pretul trebuie sa fie float")
    obiect = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
    return lista + [obiect]


def get_by_id(id, lista):
    """
    cauta obiectul cu id-ul dat in lista
    :param id: string
    :param lista: lista cu obiecte
    :return: obiectul cu id-ul primit, sau None daca nu exista
    """
    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None


def sterge_obiect(id, lista):
    """
    sterge obiectul din lista
    :param lista: lista cu obiecte
    :param id: id-ul obiectul pe care vrem sa il stergem
    :return: lista fara obiect
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Obiectul cu id-ul dat nu exista")
    return [obiect for obiect in lista if get_id(obiect) != id]


def modifica_obiect(id, nume, descriere, pret_achizitie, locatie, lista):
    """
    modifica un obiect din lista
    :param lista: lista cu obiecte
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret_achizitie: pretul obiectului
    :param locatie: locatia obiectului
    :return: lista cu obiectul modificat
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Obiectul cu id-ul dat nu exista")
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) != id:
            lista_noua.append(obiect)
        else:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret_achizitie, locatie)
            lista_noua.append(obiect_nou)
    return lista_noua
