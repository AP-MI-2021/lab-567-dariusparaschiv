from Domanin.inventar import get_pret, creeaza_obiect, get_locatie, get_descriere, get_nume, get_id


def concatenare(cuv, valoare, lista):
    """
    concateneaza un string citit la toate obiectele cu pretul mai mare decat o valoare citita
    :param cuv: stringul pt concatenare
    :param valoare: valoarea citita
    :param lista: lista cu obiectele
    :return: lista in care obiectele cu pretul mai mare decat valoarea sunt modificate
    """
    lista_noua = []
    for obiect in lista:
        if get_pret(obiect) > valoare:
            obiect_nou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect) + cuv,
                get_pret(obiect),
                get_locatie(obiect)
            )
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def verifica_locatie(locatie_initiala, locatie_finala, lista):
    """
    Verifica daca locatiile primite ca paramtru coincid cu locatiile obiectelor
    :param locatie_initiala:
    :param locatie_finala:
    :param lista: lista cu obiecte
    :return: True, daca locatiile primite ca parametru sunt valide, False in caz contar
    """
    ok_i = False
    ok_f = False
    for obiect in lista:
        if get_locatie(obiect) == locatie_initiala:
            ok_i = True
        else:
            if get_locatie(obiect) == locatie_finala:
                ok_f = True
    return ok_i and ok_f


def mutare(locatie_initiala, locatie_finala, lista):
    """
    Muta obiectele dintr-o locatie in alta
    :param locatie_initiala:
    :param locatie_finala:
    :param lista: lista cu obiecte
    :return: lista modificata dupa mutare
    """
    lista_noua = []
    for obiect in lista:
        if get_locatie(obiect) == locatie_initiala:
            obiect_nou = creeaza_obiect(
                get_id(obiect),
                get_nume(obiect),
                get_descriere(obiect),
                get_pret(obiect),
                locatie_finala
            )
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def pret_maxim_per_locatie(lista):
    """
    Determina cel mai mai pret pt fiecare locatie
    :param lista: lista cu obiecte
    :return: un dictionar 'rezultat' cu elementele formate din cheia locatie si valoarea pret
    """
    rezultat = {}
    for obiect in lista:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie in rezultat:
            if pret > rezultat[locatie]:
                rezultat[locatie] = pret
        else:
            rezultat[locatie] = pret
    return rezultat


def ordonare_pret(lista):
    """
    Ordonarea obiectelor crescator dupa pretul de achizitie
    :param lista: lista cu obiectele
    :return: lista cu obiectele ordonate
    """
    return sorted(lista, key=lambda obiect: float(get_pret(obiect)))
    # intrebare 1. de ce trebuie sa specific type la get_pret
    # intrebare 2. unde verifica ca datele sa fie bune?
    # adica daca la pret utilizatorul adauga un string, sa afisam eroare


def afisare_suma_pret_locatie(lista):
    """
    Afiseaza suma preturile pt fiecare locatie
    :param lista: lista cu obiecte
    :return: un dicitonar -rezultat-
    """
    rezultat = {}
    for obiect in lista:
        locatie = get_locatie(obiect)
        pret = float(get_pret(obiect))
        if locatie in rezultat:
            rezultat[locatie] += pret
        else:
            rezultat[locatie] = pret
    return rezultat
