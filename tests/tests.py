import unittest
import rectangle
import square
import circle
import triangle


class RectangleTests(unittest.TestCase):
    def test_area_zero(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)
    
    def test_area_negative_param(self):
        res = rectangle.area(-1, 5)
        self.assertEqual(res, -5)

    def test_area_negative_params(self):
        res = rectangle.area(-1, -5)
        self.assertEqual(res, 5)

    def test_area_basic_params(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_zero(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_param(self):
        res = rectangle.perimeter(-1, 5)
        self.assertEqual(res, 8)

    def test_perimeter_negative_params(self):
        res = rectangle.perimeter(-1, -5)
        self.assertEqual(res, -12)
    
    def test_perimeter_basic_params(self):
        res = rectangle.perimeter(10, 15)
        self.assertEqual(res, 50)
    


class TriangleTest(unittest.TestCase):
    def test_area_zero(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)
    
    def test_area_negative_param(self):
        res = triangle.area(5, -1)
        self.assertEqual(res, -2.5)

    def test_area_negative_params(self):
        res = triangle.area(-5, -1)
        self.assertEqual(res, 2.5)

    def test_area_basic_params(self):
        res = triangle.area(15, 5)
        self.assertEqual(res, 37.5)

    def test_perimeter_zero(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_param(self):
        res = triangle.perimeter(-1, 5, 7)
        self.assertEqual(res, 11)

    def test_perimeter_negative_params(self):
        res = triangle.perimeter(-1, -5, -12)
        self.assertEqual(res, -18)
    
    def test_perimeter_basic_params(self):
        res = triangle.perimeter(10, 15, 20)
        self.assertEqual(res, 45)
    
class SquareTests(unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test__area_negative_param(self):
        res = square.area(-4)
        self.assertEqual(res, 16)
    def test_area_basic(self):
        res = square.area(8)
        self.assertEqual(res, 64)

    def test_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    def test__perimeter_negative_param(self):
        res = square.perimeter(-4)
        self.assertEqual(res, -16)
    def test_perimeter_basic(self):
        res = square.perimeter(8)
        self.assertEqual(res, 32)


class CircleTest(unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_area_negative_radius(self):
        res = circle.area(-4)
        self.assertEqual(res, 50.26548245743669)
    def test_area_basic(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)
    def test_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    def test_perimeter_negative_radius(self):
        res = circle.perimeter(-4)
        self.assertEqual(res, -25.132741228718345)
    def test_perimeter_basic(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)
    

    