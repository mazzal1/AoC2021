import os
import numpy as np


def main():
    filepath = os.path.abspath(os.path.dirname(__file__))
    inputpath = os.path.join(filepath, 'input.txt')
    with open(inputpath, "r") as f:
        input = f.read()
    inputLines = input.split('\n')
    lineLength = len(inputLines[0])

    oxygenArray = inputLines.copy()
    for i in range(lineLength):
        zeroCount = 0
        oneCount = 0
        for line in oxygenArray:
            if line[i] == '0':
                zeroCount += 1
            elif line[i] == '1':
                oneCount += 1
            else:
                exit(1, 'Undefined case')
        if oneCount >= zeroCount:
            filterBit = '1'
        else:
            filterBit = '0'
        if zeroCount == 0 or oneCount == 0:
            oxygen = oxygenArray[0]
            break
        for line in oxygenArray:
            if line[i] != filterBit:
                j = oxygenArray.index(line)
                del oxygenArray[j]
        if len(oxygenArray) == 1 or i == lineLength - 1:
            oxygen = oxygenArray[0]
            break

    co2array = inputLines.copy()
    for i in range(lineLength):
        zeroCount = 0
        oneCount = 0
        for line in co2array:
            if line[i] == '0':
                zeroCount += 1
            elif line[i] == '1':
                oneCount += 1
            else:
                exit(1, 'Undefined case')
        if zeroCount <= oneCount:
            filterBit = '0'
        else:
            filterBit = '1'
        if zeroCount == 0 or oneCount == 0:
            co2 = co2array[0]
            break
        for line in co2array:
            if line[i] != filterBit:
                j = co2array.index(line)
                del co2array[j]
        if len(co2array) == 1 or i == lineLength - 1:
            co2 = co2array[0]
            break
    result = int(oxygen, 2) * int(co2, 2)
    print(result)


if __name__ == '__main__':
    main()
