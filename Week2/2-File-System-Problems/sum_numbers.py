import sys
from cat import has_arguments


def get_file_contents(filename):
    f = open(filename, 'r')
    contentst = f.read().split(" ")
    f.close()
    return contentst


def main():
    if has_arguments(1):
        s = sum([int(n) for n in get_file_contents(sys.argv[1])])
    else:
        print("There are no arguments")
    print(s)


if __name__ == "__main__":
    main()
