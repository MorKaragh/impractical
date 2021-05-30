import collections


def main():
    inpt = input("tell me something...\n")
    plot(inpt)


def plot(string):
    counter = collections.Counter(list(string))

    for i in counter:
        row = '\'' + i + '\' : ['
        for j in range(counter.get(i)):
            row += '\'' + i + '\' '
        row = row.rstrip() + ']'
        print(row)


if __name__ == '__main__':
    main()
