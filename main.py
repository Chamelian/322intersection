"""
John Maynard
CSCI 332 Spring 2025
Programming Assignment #class17
I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by the university's academic integrity policy. I understand the importance the consequences of plagiarism.
"""

# Typing

def constructPoint(x: int, y: int) -> tuple[int, int]:
    return (x, y)


def constructLine(point1: tuple[int, int], point2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    return (point1, point2)


def lineIntersection(line1: tuple[tuple[int, int], tuple[int, int]], line2: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    orientation1: int = getOrientation(line1[0], line1[1], line2[0])
    orientation2: int = getOrientation(line1[0], line1[1], line2[1])

    orientation3: int = getOrientation(line2[0], line2[1], line1[0])
    orientation4: int = getOrientation(line2[0], line2[1], line1[1])

    xAxis: bool = False
    yAxis: bool = False

    if orientation1 != orientation2 and orientation3 != orientation4:
        return True
    elif orientation1 == orientation2 == orientation3 == orientation4 == 0:
        xAxis = testAxisIntersect(line1, line2, "x")
        yAxis = testAxisIntersect(line1, line2, "y")
        return xAxis and yAxis
    else:
        return False


# Convoluted. Needs to be refactored or extensively documented
def testAxisIntersect(line1: tuple[tuple[int, int], tuple[int, int]], line2: tuple[tuple[int, int], tuple[int, int]], direction: str) -> bool:
    point1: int
    point2: int
    point3: int
    point4: int
    if direction == "x":
        point1 = line1[0][0]
        point2 = line1[1][0]
        point3 = line2[0][0]
        point4 = line2[1][0]
    elif direction == "y":
        point1 = line1[0][1]
        point2 = line1[1][1]
        point3 = line2[0][1]
        point4 = line2[1][1]
    else:
        raise ValueError

    return (
        (point1 >= point3 and point1 <= point4)
        or (point1 <= point3 and point1 >= point4)
        or (point2 >= point3 and point2 <= point4)
        or (point2 <= point3 and point2 >= point4)
        or (point1 >= point3 and point2 <= point4)
        or (point1 <= point3 and point2 >= point4)
    )


def getOrientation(point1: tuple[int, int], point2: tuple[int, int], point3: tuple[int, int]) -> int:
    orientation: int = ((point2[1] - point1[1]) * (point3[0] - point2[0])) - (
        (point3[1] - point2[1]) * (point2[0] - point1[0])
    )

    if orientation == 0:
        return 0
    elif orientation > 0:
        return 1
    else:
        return -1


if __name__ == "__main__":
    firstLine: tuple[tuple[int, int], tuple[int, int]] = constructLine(constructPoint(0, 2), constructPoint(2, 0))
    secondLine: tuple[tuple[int, int], tuple[int, int]] = constructLine(constructPoint(1, 2), constructPoint(2, 1))

    print(lineIntersection(firstLine, secondLine))
