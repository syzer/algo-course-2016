# Uses python3
import sys
from collections import namedtuple, Counter

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    for s in segments:
        for p in range(s.start, s.end + 1):
            points.append(p)
    # return Counter(points).most_common(1)
    return [x[0] for x in Counter(points).most_common(2)]


if __name__ == '__main__':
    n, *data = map(int, sys.stdin.read().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
