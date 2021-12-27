# python3

# You are responsible for collecting signatures from all 
# tenants in a building. For each tenant, you know a 
# period of time when he or she is at home. You would 
# like to collect all signatures by visiting the building 
# as few times as possible. For simplicity, we assume that 
# when you enter the building, you instantly collect the 
# signatures of all tenants that are in the building at that time.

# Input: A sequence of n ≤ 103 segments [l1, r1], ... ,[ln, rn] 
# on a line.

# Output: A set of points of minimum size such that each 
# segment [li, ri] contains a point, i.e., there exists a 
# point x such that li ≤ x ≤ ri.

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments = sorted(segments, key=lambda x: x.end)
    points = []
    endpoint = -1
    for segment in segments:
        if endpoint < segment.start:
            endpoint = segment.end
            points.append(endpoint)

    return points


def main():
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2],
                                                                 data[1::2])))
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(n)
    print(*output_points)


if __name__ == '__main__':
    main()
