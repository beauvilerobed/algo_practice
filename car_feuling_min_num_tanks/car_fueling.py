# python3

# Compute the minimum number of tank refills to get 
# from one city to another.

# Assuming that the distance between the cities is 
# 1 ≤ d ≤ 105 miles, a car can travel at most 1 ≤ m ≤ 400 
# miles on a full tank, and there are 1 ≤ n ≤ 300 gas 
# stations at distances stop1, stop2 ,..., stopn along the way, 
# output the minimum number of refills needed. Assume that the 
# car starts with a full tank. If it is not possible to reach 
# the destination, output −1. The distances to gas stations 
# satisfy the inequalities 0 < stop1 < stop2 < ⋯ < stopn < d .

def compute_min_num_of_refills(d, m, stops):
    stops = [0] + stops + [d]
    n = len(stops)
    num_refill, current_refill = 0, 0
    while current_refill < n - 1:
        last_refill = current_refill
        while (current_refill < n - 1) and (stops[current_refill + 1] -
                                            stops[last_refill] <= m):
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill < n - 1:
            num_refill += 1

    return num_refill


def main():
    input_d = int(input())
    input_m = int(input())
    input_stops = list(map(int, input().split()))

    print(compute_min_num_of_refills(input_d, input_m, input_stops))


if __name__ == '__main__':
    main()
