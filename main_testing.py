import unittest
from custom_list import CustomList


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.lst = CustomList(1, 2, 3, 4)

    def test_creating_works_correctly(self):
        self.assertEqual(str(self.lst), "1, 2, 3, 4")

    def test_append_should_work(self):
        self.lst.append(5)
        self.assertEqual(self.lst.size(), 5)

    def test_remove_should_work(self):
        self.assertEqual(self.lst.remove(3), 4)

    def test_remove_should_throw_error(self):
        with self.assertRaises(Exception): self.lst.remove(4)

    def test_get_should_work(self):
        self.assertEqual(self.lst.get(0), 1)

    def test_get_should_throw_error(self):
        with self.assertRaises(Exception): self.lst.get(4)

    def test_extend_should_work(self):
        self.assertEqual(self.lst.extend(5, 6, 7, 8), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_insert_should_work(self):
        self.lst.insert(3, 4)
        self.assertEqual(self.lst.size(), 5)

    def test_extend_throw_error(self):
        with self.assertRaises(Exception): self.lst.insert(5, 4)

    def test_pop_should_work(self):
        self.assertEqual(self.lst.pop(), 4)

    def test_pop_throw_error(self):
        self.lst.clear()
        with self.assertRaises(Exception): self.lst.pop()

    def test_clear_should_work(self):
        self.assertEqual(self.lst.clear(), [])

    def test_index_should_work(self):
        self.assertEqual(self.lst.index(1), 0)

    def test_index_should_throw_error(self):
        self.assertEqual(self.lst.index(40), 1)

    def test_count_should_work(self):
        self.assertEqual(self.lst.count(2), 1)

    def test_reverse_should_work(self):
        self.assertEqual(self.lst.reverse(), [4, 3, 2, 1])

    def test_copy_should_work(self):
        self.assertEqual(self.lst.copy(), [1, 2, 3, 4])

    def test_size_should_work(self):
        self.assertEqual(self.lst.size(), 4)

    def test_add_first_should_work(self):
        self.assertEqual(self.lst.add_first(10), [10, 1, 2, 3, 4])

    def test_dictionize_should_work(self):
        dct = self.lst.dictionize()
        self.assertEqual({1: 2, 3: 4}, dct)

    def test_move_should_work(self):
        self.assertEqual(self.lst.move(2), [3, 4, 1, 2])

    def test_sum_should_work(self):
        self.assertEqual(self.lst.sum(), 10)

    def test_overbound_should_work(self):
        self.assertEqual(self.lst.overbound(), 4)

    def test_underbound_should_work(self):
        self.assertEqual(self.lst.underbound(), 1)


if __name__ == '__main__':
    unittest.main()
