def find_smallest(array):
    smallest = array[0]  # to store the smallest value
    smallest_index = 0  # to store the index of the smallest value

    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index


def selection_sort(array):  # sorting array
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)  # finds the smallest element in an array and adds it to a new array
        new_array.append(array.pop(smallest))

    return new_array


# call function here or create your array and then call function
