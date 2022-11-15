import unittest
import trig


class TestMathMethods(unittest.TestCase):
    def test_law_of_sins(self):
        self.assertEqual(trig.law_of_sines(side_a=17, angle_a=42, side_b=22), 59.99)
        self.assertEqual(trig.law_of_sines(side_a=44, angle_a=88, angle_b=57), 36.92)

    def test_law_of_cosines(self):
        self.assertEqual(trig.law_of_cosines(side_a=23, side_b=15, angle_c=27), 11.80)
        self.assertEqual(trig.law_of_cosines(side_a=23, side_b=15, side_c=11.8), 27.01)

    def test_herons(self):
        self.assertEqual(trig.herons(side_a=100, side_b=240, side_c=260), 12000)
        self.assertEqual(trig.herons(60, 60, 60), 1558.85)

    def test_area_of_oblique_triangle(self):
        self.assertEqual(
            trig.area_of_oblique_triangle(side_a=7, side_b=10, angle_c=62), 30.9
        )

    def test_solve(self):
        self.assertEqual(
            trig.solve(sides=[3.5, 5.1, 7.9], angles=[]),
            {
                "side_a": [3.5],
                "side_b": [5.1],
                "side_c": [7.9],
                "angle_a": [132.57],
                "angle_b": [19.04],
                "angle_c": [28.39],
            },
        )  # sss
        self.assertEqual(
            trig.solve(sides=[12.6], angles=[105, 41]),
            {
                "side_a": [12.6],
                "side_b": [8.56],
                "side_c": [7.29],
                "angle_a": [105],
                "angle_b": [41],
                "angle_c": [34]
            },
        )  # aas
        self.assertEqual(
            trig.solve(sides=[16, 20], angles=[48]),
            {
                "side_a": [16],
                "side_b": [20],
                "side_c": [19.31, 7.46],
                "angle_a": [48],
                "angle_b": [68.27, 111.73],
                "angle_c": [63.73, 20.27]
            },
        )  # ssa (no bad words in math!)


if __name__ == "__main__":
    unittest.main()
