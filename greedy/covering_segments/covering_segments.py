# Uses python3
import sys
from collections import namedtuple, Counter

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    final = []

    while len(segments):
        points = []

        for s in segments:
            for p in range(s.start, s.end + 1):
                points.append(p)

        most_common = Counter(points).most_common(1)[0]
        final.append(most_common[0])

        segments = [Segment(s.start, s.end) for s in segments
                    if most_common[0] not in range(s.start, s.end + 1)]

    return final


if __name__ == '__main__':
    n, *data = map(int, sys.stdin.read().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
