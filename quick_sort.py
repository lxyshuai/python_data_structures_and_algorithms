import random


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot_index = 0
    pivot = array[pivot_index]
    less_part = [i for i in array[pivot_index + 1:] if i <= pivot]
    great_part = [i for i in array[pivot_index + 1:] if i > pivot]
    return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_quick_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    seq = quick_sort(seq)
    assert seq == sorted_seq


def partition(array, begin, end):
    pivot_index = begin
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1

    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]
    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l)) == 3


def quick_sort_inplace(array, begin, end):
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quick_sort_inplace(array, begin, pivot)
    quick_sort_inplace(array, pivot + 1, end)


def test_quick_sort_inplace():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    quick_sort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq
