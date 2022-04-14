def quick_sort(array):
    if len(array) < 2:  # base case, arrays with 0 and 1 elem sorted
        return array
    else:
        pivot = array[0]  # recursion case
        less = [i for i in array[1:] if i < pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + pivot + quick_sort(greater)


print(quick_sort([10, 5, 6, 1, 2, 3, 8]))
