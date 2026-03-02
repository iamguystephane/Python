

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if(arr[j] > arr[i]):
                arr[i], arr[j] = arr[j], arr[i];


def bin_search(arr, k):
    lb, ub = 0, len(arr) - 1;
    while(lb <= ub):
        mid = (lb + ub) // 2;
        if(arr[mid] == k):
            return mid;
        elif(arr[mid] < k):
            lb = mid + 1;
        else:
            ub = mid - 1;
    return -1;


def main():
    arr = [5, 2, 9, 1, 5, 6];
    bubble_sort(arr);
    print(f"Sorted array: {arr}");
    k = 5;
    index = bin_search(arr, k);
    if(index != -1):
        print(f"Element {k} found at index: {index}");
    else:
        print(f"Element {k} not found in the array.");

main();