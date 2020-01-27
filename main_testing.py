import unittest
from custom_list import CustomList


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.lst = CustomList(1, 2, 3, 4)

    def test_creating_works_correctly(self):
        self.assertEqual(self.lst.__str__(), [1, 2, 3, 4])

    def test_append_should_work(self):
        self.lst.append(5)
        self.assertEqual(self.lst.size(), 5)

    def test_remove_should_work(self):
        self.assertEqual(self.lst.remove(3), 4)

    def test_remove_should_not_work(self):
        self.assertRaises("No, you can't remove that. Index is out of the list.", self.lst.remove(4).exception.args[0])

    def test_pop_works_correctly(self):
        self.lst = CustomList(1, 2, 3, 4)
        self.assertEqual(self.lst.pop(), 4)


if __name__ == '__main__':
    unittest.main()
