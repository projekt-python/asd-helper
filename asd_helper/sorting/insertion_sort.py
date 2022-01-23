from typing import List, TypeVar

# TODO write propper docstrings

def insertion_sort(arr: List[int]) -> List[int]:
    # it is isnertion sort that modifies input lsit
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

    return arr