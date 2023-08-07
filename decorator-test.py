from numpy import random
from timeit import default_timer as timer
import numpy


def execution_time(sort):
    def wrapper(arr):
        start_time = timer()
        sort(arr)
        end_time = timer() - start_time

        print(f"--- {end_time} seconds ---")

    return wrapper


@execution_time
def selection_sort(arr: [float]) -> None:
    for i in range(len(arr)):
        min_ind: int = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        if min_ind != i:
            arr[min_ind], arr[i] = arr[i], arr[min_ind]


@execution_time
def bubble_sort(arr: [float]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


@execution_time
def insertion_sort(arr: [float]) -> None:
    for i in range(1, len(arr)):
        curr = arr[i]
        j: int = i - 1
        while j > -1 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr


mylist1 = (numpy.random.uniform(-100000, 100000, size=10))
mylist2 = (numpy.random.uniform(-100000, 100000, size=10))
mylist3 = (numpy.random.uniform(-100000, 100000, size=10))

print(f"selection sort:")
selection_sort(mylist1)
print(mylist1)

print(f"\nbubble sort:")
selection_sort(mylist2)
print(mylist2)

print(f"\ninsertion sort:")
selection_sort(mylist3)
print(mylist3)
