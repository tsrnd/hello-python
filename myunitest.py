import unittest
import mymodule

class MyUnitest(unittest.TestCase):
    def test_random_list(self):
        self.assertEqual(len(mymodule.randomList()),10000)

    def test_list_sorted(self):
        list_not_sort = mymodule.randomList()
        list_sorted = list_not_sort.copy()
        list_not_sort.sort
        mymodule.budle_sort(list_sorted)
        self.assertEqual(list_not_sort,list_not_sort)

if __name__ == "__main__":
    unittest.main()
