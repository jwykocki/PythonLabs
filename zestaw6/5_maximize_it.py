#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product


def maximize_expression_value(arrays, m):
    all_combinations = product(*arrays)

    max_value = max(sum(x ** 2 for x in combination) % m for combination in all_combinations)

    return max_value


if __name__ == '__main__':
    n, m = map(int, input().split())

    arrays = [list(map(int, input().split()[1:])) for _ in range(n)]

    result = maximize_expression_value(arrays, m)
    print(result)
