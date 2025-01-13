from main2 import Segment

# I have a Segment [10,20)
# Meet it with different maps
# 01. [ 1, 5) => ([],       [[10,20)])          no overlap
# 02. [ 1,10) => ([],       [[10,20)])          no overlap
# 03. [ 1,15) => ([[10,15)],[[15,20)])          overlap
# 04. [ 1,20) => ([[10,20)],[[ 1,10)])          overlap
# 05. [ 1,25) => ([[10,20)],[[ 1,10), [20,25)]) overlap
# 06. [10,15) => ([[10,15)],[])                 overlap
# 07. [10,20) => ([[10,20)],[])                 overlap
# 08. [10,25) => ([[10,20)],[[20,25)])          overlap
# 09. [15,17) => ([[15,17)],[])                 overlap
# 10. [15,20) => ([[15,20)],[])                 overlap
# 11. [15,25) => ([[15,20)],[[20,25)])          overlap
# 12. [20,25) => ([],       [[20,25)])          no overlap
# 13. [22,25) => ([],       [[22,25)])          no overlap

RESULT: dict[tuple[int, int], tuple[list[Segment], list[Segment]]] = {
    (1, 2): ([], [Segment(start=10, end=20)]),
    (1, 10): ([], [Segment(start=10, end=20)]),
    (1, 15): ([Segment(start=10, end=15)], [Segment(start=15, end=20)]),
    (1, 20): ([Segment(start=10, end=20)], []),
    (1, 25): ([Segment(start=10, end=20)], []),
    (10, 15): ([Segment(start=10, end=15)], [Segment(start=15, end=20)]),
    (10, 20): ([Segment(start=10, end=20)], []),
    (10, 25): ([Segment(start=10, end=20)], []),
    (15, 17): (
        [Segment(start=15, end=17)],
        [Segment(start=10, end=15), Segment(start=17, end=20)],
    ),
    (15, 20): ([Segment(start=15, end=20)], [Segment(start=10, end=15)]),
    (15, 25): ([Segment(start=15, end=20)], [Segment(start=10, end=15)]),
    (20, 25): ([], [Segment(start=10, end=20)]),
    (22, 25): ([], [Segment(start=10, end=20)]),
}


# def test_case1():
#     s1 = Segment(start=10, end=20)
#     start,end = 1,2
#     s2 = Segment(start=start, end=end)
#     print(f"s1 = {s1} s2 = {s2}")
#     result = s1.meet(s2)
#     assert len(result) == 2
#     expected = RESULT[(start,end)]
#     print(f"result = {result} expected = {expected}")
#     assert all([a == b for a, b in zip(result[0], expected[0])])
#     assert all([a == b for a, b in zip(result[1], expected[1])])


def test_cases():
    s1 = Segment(start=10, end=20)
    for start, end in RESULT:

        s2 = Segment(start=start, end=end)
        actual = s1.meet(s2)
        assert len(actual) == 2
        expected = RESULT[(start, end)]
        print(f"s2 = {s2} actual = {actual} expected = {expected}")
        assert str(actual[0]) == str(expected[0])
        assert str(actual[1]) == str(expected[1])
