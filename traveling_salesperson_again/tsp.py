# python3

# This folder contains a program that finds the minimum cost tour (approx.) 
# for a travelling salesman i.e. given n vertices, it finds a minimum cost 
# tour (a cyclic path) that visits all vertices by using the Nearest Neighbor 
# heuristic. Since a heuristic is used, the answer is not the absolute optimal 
# but in close range to it. Also, the running time of this heuristic is O(n^2) 
# instead of the O(n^2 * 2^n) achieved by the proper soltuion.


from file_reader import read_file, get_graph


def tsp(graph, n):
    visited = [1]
    distance = 0

    while len(visited) < n:
        unvisited = set(range(1, n+1)) - set(visited)
        index = visited[-1]
        minimum, j = min([(graph[index, j], j) for j in unvisited])
        distance += minimum
        visited.append(j)
    
    return int(distance + graph[visited[-1], 1])


def main():
    cities, n = read_file('cities.txt')
    graph = get_graph(cities, n)
    print(tsp(graph, n) == 23)


if __name__ == '__main__':
    main()
    