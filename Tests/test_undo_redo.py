from Domanin.inventar import creeaza_obiect


def test_undo_redo():
    # 1
    lista_mare = []
    undo_list = []
    redo_list = []

    # 2
    lista = creeaza_obiect('1', 'carte', 'mat', 10.6, 'EE22')
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22']]

    # 3
    lista = creeaza_obiect('2', 'carte', 'mat', 72.3, 'EE22')
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22']]

    # 4
    lista = creeaza_obiect('3', 'carte', 'mat', 21.3, 'EE22')
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22'],
                          ['3', 'carte', 'mat', 21.3, 'EE22']]

    # 5
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22']]

    # 6
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22']]

    # 7
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == []

    # 8
    redo_list.append(lista_mare)
    if len(undo_list) > 0:
        lista_mare = undo_list.pop()
    assert lista_mare == []

    # 9
    lista = creeaza_obiect('1', 'carte', 'mat', 10.6, 'EE22')
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22']]
    lista = creeaza_obiect('2', 'carte', 'mat', 72.3, 'EE22')
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22']]
    lista = creeaza_obiect('3', 'carte', 'mat', 21.3, 'EE22')
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22'],
                          ['3', 'carte', 'mat', 21.3, 'EE22']]

    # 10
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
        assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                              ['2', 'carte', 'mat', 72.3, 'EE22'],
                              ['3', 'carte', 'mat', 21.3, 'EE22']]

    # 11  2x undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22']]
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22']]

    # 12  redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22']]
    # 13  redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
        assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                              ['2', 'carte', 'mat', 72.3, 'EE22'],
                              ['3', 'carte', 'mat', 21.3, 'EE22']]
    # 14 2 x undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['2', 'carte', 'mat', 72.3, 'EE22']]
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22']]

    # 15 add 04
    lista = creeaza_obiect('4', 'carte', 'mat', 21.1, 'EE22')
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['4', 'carte', 'mat', 21.1, 'EE22']]

    # 16 redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['4', 'carte', 'mat', 21.1, 'EE22']]

    # 17 undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22']]

    # 18 undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == []

    # 19 redo redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22']]

    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['4', 'carte', 'mat', 21.1, 'EE22']]

    # 20 redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [['1', 'carte', 'mat', 10.6, 'EE22'],
                          ['4', 'carte', 'mat', 21.1, 'EE22']]
