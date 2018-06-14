# -*- coding: utf-8 -*-
import random


def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    bubble_sort(seq)
    assert seq == sorted_seq


def select_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    select_sort(seq)
    assert seq == sorted_seq


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value


def test_insertion_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    insertion_sort(seq)
    assert seq == sorted_seq
