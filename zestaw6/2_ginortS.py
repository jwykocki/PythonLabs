#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

if __name__ == '__main__':
    s = input()


def ginorts_sort(char):
    if char.islower():
        return (0, char)
    elif char.isupper():
        return (1, char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            return (2, char)
        else:
            return (3, char)


sorted_string = ''.join(sorted(s, key=ginorts_sort))

print(sorted_string)

