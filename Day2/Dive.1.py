import os


def main():
    filepath = os.path.abspath(os.path.dirname(__file__))
    inputpath = os.path.join(filepath, 'input.txt')
    with open(inputpath, "r") as f:
        input = f.read()
    inputLines = input.split('\n')
    x = 0
    y = 0
    for line in inputLines:
        command = line.split(' ')[0]
        value = int(line.split(' ')[1])
        if (command == 'forward'):
            x = x + value
        elif (command == 'down'):
            y = y + value
        elif(command == 'up'):
            y = y - value
        else:
            exit(1, 'wrong command')
    print(x*y)


if __name__ == '__main__':
    main()
