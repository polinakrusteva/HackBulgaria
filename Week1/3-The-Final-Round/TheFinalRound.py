def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def count_words(arr):
    result = {}
    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
# return{key:words.count(key) for key in words}


def unique_words_count(arr):
    return sum([1 for key in count_words(arr)])


def nan_expand(times):
    if times == 0:
        return ""
    result = ""
    n = "Not a "
    for x in range(0, times):
            result += n
    result += "NaN"
    return result


# def iterations_of_nan_expand2(expanded):
#     nan_table = {}
#     n = len(expanded)

#     current_index = 0

# while True:
#         current_expand = nan_expand(current_index)
#         nan_table[current_expand] = current_index

#         if len(current_expand) > n:
#             break

#     if expanded in nan_table:
#         return nan_table[expanded]

#     return False


def iterations_of_nan_expand(expanded):
    if expanded == "":
        return 0
    if expanded.count("Not a Nan") == 0:
        return False
    else:
        return expanded.count("Not a")


def next_prime(n):
    n += 1

    while not is_prime(n):
        n += 1

    return n


def divide_count(n, k):
    times = 0

    while n != 1 and n % k == 0:
        times += 1
        n = n // k

    return times


def prime_factorization(n):
    result = []

    current_prime = 2

    while n != 1:
        times = divide_count(n, current_prime)

        if times != 0:
            result.append((current_prime, times))
            n = n // current_prime ** times

        current_prime = next_prime(current_prime)

    return result


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and items[index] == first:
        result.append(items[index])
        index += 1

    return result


def group(items):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])


def oddeven(item):
    if item % 2 == 0:
        return "Even"
    else:
        return "Odd"


def groupby(func, seq):
    result = {}
    for item in seq:
        result[func(item)] = [item]
    return result


def prepare_meal(number):
    if number == 0:
        return ''
    meal = []
    while number % 3 == 0:
        meal.append("spam")
        number //= 3
    if number % 5 == 0:
        if meal != []:
            meal.append("and")
        meal.append("eggs")
    return " ".join(meal)


def is_an_bn(word):
    if word == "":
        return True
    i = 1
    acount = 0
    if word[0] == 'a':
        while str(word[i]) == 'a' and i <= str(word):
            acount += 1
            i += 1
    else:
        return False
    bcount = sum([1 for j in range(acount, len(word)) if word[i] == 'b'])
    return acount == bcount


def reduce_file_path(path):
    result = []
    parts = [part for part in path.split("/") if part not in ["", "."]]

    while len(parts) != 0:
        part = parts.pop()
        if part == ".." and len(parts) != 0:
            parts.pop()
        else:
            print(parts)
    return result
