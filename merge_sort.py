import random


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)

    left_half = merge_sort(seq[:mid])
    right_half = merge_sort(seq[mid:])

    new_seq = merge_sorted_list(left_half, right_half)
    return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    new_sorted_seq = []
    length_a = len(sorted_a)
    length_b = len(sorted_b)
    a = 0
    b = 0

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    while a < length_a:
        new_sorted_seq.append(sorted_a[a])
        a += 1

    while b < length_b:
        new_sorted_seq.append(sorted_b[b])
        b += 1

    return new_sorted_seq


def test_merge_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    seq = merge_sort(seq)
    assert seq == sorted_seq


test_merge_sort()