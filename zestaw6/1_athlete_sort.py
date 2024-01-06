#https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda y: y[k])

    # Print the sorted table
    for row in arr:
        print(" ".join(map(str, row)))