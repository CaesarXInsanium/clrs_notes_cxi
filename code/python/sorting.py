import sys
import random
import math


def find_smallest(A: list):
    smallest_idx = 0
    for (i, x) in enumerate(A):
        if x < A[smallest_idx]:
            smallest_idx = i
    return smallest_idx


def selection_sort(A):
    if len(A) == 1:
        return A
    small_idx = find_smallest(A)
    A[0], A[small_idx] = A[small_idx], A[0]
    result = [A[0]]
    result.extend(selection_sort(A[1:]))
    return result


def selection_sort_test():
    import random
    array = [random.randint(0, 100) for i in range(100)]
    print(array)
    print(selection_sort(array))


def insertion_sort(A):
    array = A.__len__() - 1
    for j in range(2, array):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i], A[i+1] = A[i+1], A[i]
            i = i-1
        A[i+1] = key
    return A


def insertion_sort_test():
    import random
    array = [random.randint(0, 100) for i in range(100)]
    print(array)
    print(insertion_sort(array))


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = list()
    R = list()
    for i in range(1, n1):
        L[i] = A[p + i - 1]
    for j in range(1, n2):
        R[j] = A[q + j]

    L[n1 + 1] = sys.maxsize
    R[n2 + 1] = sys.maxsize

    i = 1
    j = 1
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[j]
            i = i + 1
        elif A[k] == R[j]:
            j = j + 1
    return A


def merge_sort(A, p, r):

    if p < r:
        q = math.floor((p+r)/2)
        a1 = merge_sort(A, p, q)
        a2 = merge_sort(A, q+1, r)
        merge(a1+a2, p, q, r)
    return A


if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(100)]
    print(array)
    print(selection_sort(array))
