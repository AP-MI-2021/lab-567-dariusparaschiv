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
