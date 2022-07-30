def find_smallest(A:list):
    smallest_idx = 0
    for (i,x) in enumerate(A):
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
    l = [random.randint(0,100) for i in range(100)]
    print(l)
    print(selection_sort(l))

def insertion_sort(A):
    l = A.__len__() -1
    for j in range(2,l):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i], A[i+1] = A[i+1], A[i]
            i = i-1
        A[i+1] = key
    return A

def insertion_sort_test():
    import random
    l = [random.randint(0,100) for i in range(100)]
    print(l)
    print(insertion_sort(l))
def merge_sort(A, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q

    L = [None for _ in range(n_1 + 1)]
    R= [None for _ in range(n_2 + 1)]

    for i in range(0,n_1 + 1):
        L[i] = A[p + i - 1]

    for j in range(0,n_2 + 1):
        R[j] = A[q + j]

if __name__ == "__main__":
    insertion_sort_test()
