import os
import numpy as np


def main():
    filepath = os.path.abspath(os.path.dirname(__file__))
    inputpath = os.path.join(filepath, 'input.txt')
    with open(inputpath, "r") as f:
        input = f.read()
    inputLines = input.split('\n')
    lineLength = len(inputLines[0])
    zeroCount = np.zeros(lineLength)
    oneCount = np.zeros(lineLength)
    for line in inputLines:
        for i in range(lineLength):
            if line[i] == '0':
                zeroCount[i] += 1
            elif line[i] == '1':
                oneCount[i] += 1
            else:
                exit(1, 'Wrong input')
    gammaString = ''
    epsilonString = ''
    for i in range(lineLength):
        if zeroCount[i] > oneCount[i]:
            gammaString += '0'
            epsilonString += '1'
        elif zeroCount[i] < oneCount[i]:
            gammaString += '1'
            epsilonString += '0'
        else:
            exit(1, 'Undefined input case')
    gamma = int(gammaString, 2)
    epsilon = int(epsilonString, 2)
    result = gamma * epsilon
    print(result)


if __name__ == '__main__':
    main()
