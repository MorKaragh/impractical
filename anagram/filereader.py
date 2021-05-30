import sys


def read_file(file):
    try:
        with open(file) as in_file:
            text = in_file.read().split('\n')
            text = [x.lower() for x in text]
            return text
    except IOError as e:
        print("{} Ошибка при открытии {}".format(e, file), file=sys.stderr)
