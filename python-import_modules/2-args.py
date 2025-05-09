#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("{} argument".format(len(sys.argv)-1))
else:
    print("{} arguments".format(len(sys.argv)-1))
for i in sys.argv[1:]:
    print(i)
