# from covering_segments import *
from covering_segments_fast import *

# test 2
segments = [(3, 5), (3, 7), (3, 9)]
segments = [Segment(s[0], s[1]) for s in segments]
assert (len(optimal_points(segments)) == 1)

# test 3
segments = [(2, 8), (2, 8), (2, 8)]
segments = [Segment(s[0], s[1]) for s in segments]
assert (len(optimal_points(segments)) == 1)

# test 4
segments = [Segment(s[0], s[1]) for s in [(0, 100), (2, 8), (2, 8)]]
assert (len(optimal_points(segments)) == 1)

# test 5
segments = [Segment(s[0], s[1]) for s in [(1, 3), (2, 5), (3, 6)]]
assert (len(optimal_points(segments)) == 1)

# test 6
segments = [Segment(s[0], s[1]) for s in [(4, 7), (1, 3), (2, 5), (5, 6)]]
assert (len(optimal_points(segments)) == 2)
# TODO [1000000000, 1000000000]

# test 7
segments = [Segment(s[0], s[1]) for s in [(5, 20), (3, 7), (4, 10), (2, 6)]]
assert (len(optimal_points(segments)) == 1)

# 43
segments = [
    (41, 42), (52, 52), (63, 63), (80, 82), (78, 79), (35, 35), (22, 23), (31, 32), (44, 45), (81, 82), (36, 38),
    (10, 12), (1, 1), (23, 23), (32, 33), (87, 88), (55, 56), (69, 71), (89, 91), (93, 93), (38, 40), (33, 34),
    (14, 16), (57, 59), (70, 72), (36, 36), (29, 29), (73, 74), (66, 68), (36, 38), (1, 3), (49, 50), (68, 70),
    (26, 28), (30, 30), (1, 2), (64, 65), (57, 58), (58, 58), (51, 53), (41, 41), (17, 18), (45, 46), (4, 4), (0, 1),
    (65, 67), (92, 93), (84, 85), (75, 77), (39, 41), (15, 15), (29, 31), (83, 84), (12, 14), (91, 93), (83, 84),
    (81, 81), (3, 4), (66, 67), (8, 8), (17, 19), (86, 87), (44, 44), (34, 34), (74, 74), (94, 95), (79, 81), (29, 29),
    (60, 61), (58, 59), (62, 62), (54, 56), (58, 58), (79, 79), (89, 91), (40, 42), (2, 4), (12, 14), (5, 5), (28, 28),
    (35, 36), (7, 8), (82, 84), (49, 51), (2, 4), (57, 59), (25, 27), (52, 53), (48, 49), (9, 9), (10, 10), (78, 78),
    (26, 26), (83, 84), (22, 24), (86, 87), (52, 54), (49, 51), (63, 64), (54, 54), (1000, 1020), (1001, 1002),
    (1002, 1008), (666, 666), (666, 667), (666, 668), (667, 668)
]
segments = [Segment(s[0], s[1]) for s in segments]
print(len(optimal_points(segments)))
print(optimal_points(segments))

# __name__ == '__main__'
