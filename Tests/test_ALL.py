from Tests.test_CRUD import test_adauga_obiect, test_modifica_obiect, test_sterge_obiect
from Tests.test_domain import test_obiect
from Tests.test_functionalitati import test_concatenare


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_modifica_obiect()
    test_sterge_obiect()
    test_concatenare()
