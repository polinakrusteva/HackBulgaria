import sys
from cat import has_arguments
import os


def to_gb(n):
    return n / (10 ** -9)


def main():
    if has_arguments(1):
        path = sys.argv[1]
        byte_size = 0
        for root, subsirs, files in os.walk(path):
            for file_to_count in files:
                try:
                    byte_size += os.path.getsize(os.path.join(root, file_to_count))
                except FileNotFoundError as error:
                    print(error)
        print(to_gb(byte_size))
    else:
        print("There are no arguments.")


if __name__ == "__main__":
    main()
