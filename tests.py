import unittest
import trig


class TestMathMethods(unittest.TestCase):
    def test_law_of_sins(self):
        self.assertEqual(trig.law_of_sines(
            side_a=17, angle_a=42, side_b=22), 59.99)
        self.assertEqual(trig.law_of_sines(
            side_a=44, angle_a=88, angle_b=57), 36.92)

    def test_law_of_cosines(self):
        self.assertEqual(trig.law_of_cosines(
            side_a=23, side_b=15, angle_c=27), 11.80)
        self.assertEqual(trig.law_of_cosines(
            side_a=23, side_b=15, side_c=11.8), 27.01)

    def test_herons(self):
        self.assertEqual(trig.herons(
            side_a=100, side_b=240, side_c=260), 12000)
        self.assertEqual(trig.herons(60, 60, 60), 1558.85)

    def test_area_of_oblique_triangle(self):
        self.assertEqual(trig.area_of_oblique_triangle(
            side_a=7, side_b=10, angle_c=62), 30.9)


if __name__ == "__trig__":
    unittest.main()
