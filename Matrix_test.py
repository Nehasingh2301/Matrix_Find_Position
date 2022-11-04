import unittest
from Matrix import search_in_matrix


class MatrixTestCase (unittest.TestCase):
    def testSearchInMatrixValidDataFindPosition(self):
        #Arrange
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004]
        ]

        target = 100
        expectedValue=[4,1]
        #Act
        result=search_in_matrix(matrix,target)

        #Assert
        self.assertEqual(expectedValue,result)

    def testSearchInMatrixValidDataTargetNotAvailiable(self):
        #Arrange
        matrix = [
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004]
        ]

        target = 9999
        expectedValue=[-1,-1]
        #Act
        result=search_in_matrix(matrix,target)

        #Assert
        self.assertEqual(expectedValue,result)

    def testSearchInMatrixIsEmpty_returned_expectedValue(self):
        #Arrange
        matrix = []

        target = 9999
        expectedValue=[-1,-1]
        #Act
        result=search_in_matrix(matrix,target)

        #Assert
        self.assertEqual(expectedValue,result)

    def testSearchInMatrixIsNotUnique_returned_ValidationMessage(self):
        #Arrange
        matrix = [
            [1, 4, 4, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004]
        ]

        target = 9999
        expectedValue='Item of Matrix is not unique'
        #Act
        result=search_in_matrix(matrix,target)

        #Assert
        self.assertEqual(expectedValue,result)