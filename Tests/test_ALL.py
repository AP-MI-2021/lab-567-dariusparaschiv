from Tests.test_CRUD import test_adauga_obiect, test_modifica_obiect, test_sterge_obiect, test_get_by_id
from Tests.test_domain import test_obiect
from Tests.test_functionalitati import test_concatenare, test_mutare, test_pret_maxim_per_locatie, test_ordonare_pret, \
    test_afisare_suma_pret_locatie
from Tests.test_undo_redo import test_undo_redo


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_modifica_obiect()
    test_sterge_obiect()
    test_get_by_id()
    test_concatenare()
    test_pret_maxim_per_locatie()
    test_ordonare_pret()
    test_afisare_suma_pret_locatie()
    test_mutare()
    test_undo_redo()
