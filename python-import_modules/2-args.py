#!/usr/bin/python3
import sys
if len(sys.argv) - 1 == 1:
    print("{} argument :".format(len(sys.argv)-1))
if len(sys.argv) - 1 == 0:
    print("0 arguments.")
else:
    print("{} arguments :".format(len(sys.argv)-1))
for i in sys.argv[1:]:
    print(i)
