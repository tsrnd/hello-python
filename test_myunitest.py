import mymodule


def test_random_list():
    assert len(mymodule.randomList()), 10000


def test_list_sorted():
    list_not_sort = mymodule.randomList()
    list_sorted = list_not_sort.copy()
    list_not_sort.sort
    mymodule.budle_sort(list_sorted)
    assert list_not_sort, list_not_sort

def test_gnome_sort():
    list_not_sort = mymodule.randomList()
    list_sorted = list_not_sort.copy()
    list_not_sort.sort
    mymodule.gnome_sort(list_sorted)
    assert list_not_sort, list_not_sort
