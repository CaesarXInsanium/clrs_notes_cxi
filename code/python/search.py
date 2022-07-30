import sorting


def binary_search(A, key):
    """
    Implementation of binary search
    Input a SORTED list and a valid key to search for
    """
    if len(A) == 1 and A[0] == key:
        return 0
    else:
        m = len(A) // 2
    if A[m] == key:
        return m
    elif A[m] > key:
        return binary_search(A[m:], key) + m
    elif A[m] < key:
        return binary_search(A[0:m], key)
    else:
        return -1


if __name__ == "__main__":
    import random
    f = [random.randint(0, 100) for _ in range(100)]
    f = sorting.selection_sort(f)
    key = random.randint(0, 100)
    print(f)
    print(binary_search(f, key))
