#!/usr/bin/env python3
import numpy as np
import os


def main():
    filepath = os.path.abspath(os.path.dirname(__file__))
    inputpath = os.path.join(filepath, 'input.txt')
    with open(inputpath, "r") as f:
        input = f.read()
    array = np.array(input.split('\n'), dtype=np.int32)

    count = 0
    for i in range(len(array)-1):
        if array[i+1] > array[i]:
            count = count + 1
    print(count)


if __name__ == '__main__':
    main()
