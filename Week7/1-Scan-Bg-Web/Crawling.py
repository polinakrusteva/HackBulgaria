class Histogram:

    def __init__(self):
        self.__dict = {}

    def add(self, name):
        if name not in self.__dict:
            self.__dict[name] = 0
        if name in self.__dict.keys():
            self.__dict[name] += 1
        return self.__dict

    def count(self, name):
        if name not in self.__dict:
            return None
        return self.__dict[name]

    def get_dict(self):
        return self.__dict

    def items(self):
        return self.__dict.items()

    def __str__(self):
        return str(self.__dict)

    def __repr__(self):
        return self.__str__()


def main():
    h = Histogram()
    h.add("Apache")
    h.add("Apache")
    h.add("nginx")
    h.add("IIS")
    h.add("nginx")

    print(h.count("nginx"))
    print(h.count("Apache"))
    print(h.count("IIS"))
    print(h.get_dict())

    for key, count in h.items():
        print("{}: {}".format(key, count))


if __name__ == "__main__":
    main()
