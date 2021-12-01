#!/usr/bin/env python3
import numpy as np


def main():
    filename = 'input.txt'
    f = open(filename, "r")
    input = f.read()
    f.close()
    array = np.array(input.split('\n'), dtype=np.int32)

    count = 0
    for i in range(len(array)-3):
        if array[i+3] > array[i]:
            count = count + 1
    print(count)


if __name__ == '__main__':
    main()
