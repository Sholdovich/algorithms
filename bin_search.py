from math import floor


def binary_search(array, item):
    lower_bound = 0
    upper_bound = len(array)
    mid = floor((lower_bound + upper_bound) / 2)

    while array[mid] != item:
        if array[mid] < item:
            mid += 1
        elif array[mid] > item:
            mid -= 1

    print("Found %s at position %s" % (item, mid))

# create your list here:
# call function down
