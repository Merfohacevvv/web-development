import math


def arg_min(row, S):
    aMin = -1
    m = math.inf
    for i, t in enumerate(row):
        if t < m and i not in S:
            m = t
            aMin = i

    return aMin


def alg(matrix, start, end):

    dimension = len(matrix)
    row = [math.inf] * dimension

    v = start   #стартовая вершина
    S = {v}    #просмотренные вершины
    row[v] = 0
    M = [0] * dimension

    while v != -1:
        for j, dw in enumerate(matrix[v]):
            if j not in S:
                w = row[v] + dw
                if w < row[j]:
                    row[j] = w
                    M[j] = v

        v = arg_min(row, S)
        if v >= 0:
            S.add(v)

    way = [end]
    len_route = row[end]
    while end != start:
        end = M[way[-1]]
        way.append(end)
        if len(way) == dimension*dimension:
            way = None
            break
    if way is not None:
        way.reverse()
        result = {"route": way, "len_route": len_route}
    else:
        result = None


    return result

if __name__ == '__main__':
    matrix = [[0, 3, math.inf, 2, math.inf, 7],
        [math.inf, 0, math.inf, math.inf, math.inf, math.inf],
        [8, math.inf, 0, 1, 4, math.inf],
        [math.inf, math.inf, math.inf, 0, math.inf, 1],
        [math.inf, math.inf, math.inf, 2, 0, 5],
        [math.inf, math.inf, math.inf, math.inf, math.inf, 0]]

    alg(matrix, 0, 5) # {'route': [0, 3, 5], 'len_route': 3}
