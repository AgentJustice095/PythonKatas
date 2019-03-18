import unittest
import Kata02_1

class TestStringMethods(unittest.TestCase):

    def test_chop_valueexists(self):

        #Arrange
        testarray = [1, 5, 44, 45, 51, 600, 710, 711, 900]
        for x in range(0,8):
            searchvalue = testarray[x]

            #Act
            chopresult = Kata02_1.chop(searchvalue, testarray)

            #Assert
            self.assertEqual(x, chopresult, "Not found")
    def test_chop_valuenoexists(self):

        #Arrange
        testarray = [1, 5, 44, 45, 51, 600, 710, 711, 900]
        searchvalue = 60

        #Act
        chopresult = Kata02_1.chop(searchvalue, testarray)

        #Assert
        self.assertEqual(-1, chopresult, "Not found")

if __name__ == '__main__':
    unittest.main()