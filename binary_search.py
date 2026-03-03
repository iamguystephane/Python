"""Binary Search Algorithm Implementation
This code demonstrates the implementation of the binary search algorithm."""


def bubble_sort(arr):
    """Sorts the array using bubble sort algorithm."""
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bin_search(arr, k):
    """Performs binary search on the sorted array."""
    lb, ub = 0, len(arr) - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] < k:
            lb = mid + 1
        else:
            ub = mid - 1
    return -1


def main():
    """Main function to demonstrate binary search."""
    arr = [5, 2, 9, 1, 5, 6]
    bubble_sort(arr)
    print(f"Sorted array: {arr}")
    k = 5
    index = bin_search(arr, k)
    if index != -1:
        print(f"Element {k} found at index: {index}")
    else:
        print(f"Element {k} not found in the array.")


main()