#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    i = 1
    res = 0
    while i <= (count - 1):
        y = int(sys.argv[i])
        res += y
        i += 1
    print("{}".format(res))
