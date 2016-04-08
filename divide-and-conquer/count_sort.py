from collections import Counter


def sort_count(arr):
    # TODO make in line-by-line
    counts = sorted(Counter(arr).most_common(), key=lambda t: t[0])

    output = []
    for (n, count) in counts:
        output = output + [n] * count

    return output



