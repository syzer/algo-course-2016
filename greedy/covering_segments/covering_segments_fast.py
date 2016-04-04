# Uses python3
import sys
from collections import namedtuple, Counter

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    final = []

    while len(segments):
        end_min = min(s.end for s in segments)
        final.append(end_min)

        segments = [Segment(s.start, s.end) for s in segments
            if end_min not in range(s.start, s.end + 1)]

    return final


if __name__ == '__main__':
    n, *data = map(int, sys.stdin.read().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
