import sys

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

first = num(sys.argv[1])
second = num(sys.argv[2])
for i in range(first, second):
    for j in range(100):
        for k in range(100):
            print(i, j, k)
