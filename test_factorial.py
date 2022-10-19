import unittest

from Factorial import *


class Test(unittest.TestCase):
    def testCase_0(self):
        with self.assertRaises(ElementNotFoundException):
            lista = [0]
            result = search(lista, 2)

    def testCase_1(self):
        lista = [2]
        result = search(lista, 2)
        self.assertEqual(result, 0)

    def testCase_2(self):
        lista = [2, 4, 6, 8]
        result = search(lista, 4)
        self.assertEqual(result, 1)

    def testCase_3(self):
        lista = [1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18]

        result = search(lista, 15)
        self.assertEqual(result, 9)

    def testCase_4(self):
        lista = [1, 3, 5, 7, 9]
        result = search(lista, 9)
        self.assertEqual(result, 4)

    def testCase_40(self):
        with self.assertRaises(ElementNotFoundException):
            lista = [1, 3, 5, 7, 9]
            result = search(lista, 50)

    def testCase_6(self):
        with self.assertRaises(InvalidInputException):
            lista = []
            result = search(lista, 2)


if __name__ == "__main__": # pragma: no cover
    unittest.main()
