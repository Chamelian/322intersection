"""
John Maynard
CSCI 332 Spring 2025
Programming Assignment #class17
I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by the university's academic integrity policy. I understand the importance the consequences of plagiarism.
"""

import unittest

from main import Line, constructLine, constructPoint, lineIntersection


class TestLineIntersection(unittest.TestCase):
    def test_basic_intersect1(self) -> None:
        line1: Line = constructLine(constructPoint(0, 2), constructPoint(2, 0))
        line2: Line = constructLine(constructPoint(1, 2), constructPoint(2, 0))
        self.assertEqual(lineIntersection(line1, line2), True)

    def test_basic_intersect2(self) -> None:
        line1: Line = constructLine(constructPoint(0, 4), constructPoint(2, 0))
        line2: Line = constructLine(constructPoint(1, 2), constructPoint(2, 0))
        self.assertEqual(lineIntersection(line1, line2), True)

    def test_basic_intersect3(self) -> None:
        line1: Line = constructLine(constructPoint(0, 4), constructPoint(2, 0))
        line2: Line = constructLine(constructPoint(1, 2), constructPoint(3, -2))
        self.assertEqual(lineIntersection(line1, line2), True)

    def test_basic_intersect4(self) -> None:
        line1: Line = constructLine(constructPoint(0, 4), constructPoint(3, -2))
        line2: Line = constructLine(constructPoint(1, 2), constructPoint(2, 0))
        self.assertEqual(lineIntersection(line1, line2), True)

    def test_basic_intersect5(self) -> None:
        line1: Line = constructLine(constructPoint(0, 4), constructPoint(3, -2))
        line2: Line = constructLine(constructPoint(6, 2), constructPoint(4, 0))
        self.assertEqual(lineIntersection(line1, line2), False)

    def test_basic_intersect6(self) -> None:
        line1: Line = constructLine(constructPoint(2, 4), constructPoint(5, 2))
        line2: Line = constructLine(constructPoint(6, 2), constructPoint(4, 0))
        self.assertEqual(lineIntersection(line1, line2), False)

    def test_basic_intersect7(self) -> None:
        line1: Line = constructLine(constructPoint(2, 4), constructPoint(5, 2))
        line2: Line = constructLine(constructPoint(6, 6), constructPoint(4, 0))
        self.assertEqual(lineIntersection(line1, line2), True)


if __name__ == "__main__":
    unittest.main()
