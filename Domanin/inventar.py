def creeaza_obiect(id, nume, descriere, pret_achizitie, locatie):
    """
    creeaza un dictionar ce reprezinta un invetar
    :param id: string
    :param nume: string
    :param descriere: string
    :param pret_achizitie: float
    :param locatie: string
    :return: dictionarul ce contine inventarul
    """
    return{
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret_achizitie,
        "locatie": locatie
    }


def get_id(obiect):
    """
    returneaza id-ul
    :param obiect: dictionar ce contine un obiect
    :return: id-ul obiectului
    """
    return obiect["id"]


def get_nume(obiect):
    return obiect["nume"]


def get_descriere(obiect):
    return obiect["descriere"]


def get_pret(obiect):
    return obiect["pret"]


def get_locatie(obiect):
    return obiect["locatie"]


def to_string(obiect):
    return "id: {}, nume: {}, descriere: {}, pret: {}, locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )











