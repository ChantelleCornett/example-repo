import math
trial_list = [27, -3, 4,5,35,2,1,-40,7,18,9,-1, 16, 100]

# linear search is relevant because the list is not in order

def linear_search(list, target):
    for index, item in enumerate(list):
        if item == target:
            return index
    return None

print(linear_search(trial_list, 9))

def insertion_sort(lst):
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

print(insertion_sort(trial_list))

# quicker than regular linear search

def sentinelSearch(arr, n, key):

    last = arr[n - 1]

    arr[n - 1] = key
    i = 0

    while (arr[i] != key):
        i += 1

    arr[n - 1] = last

    if ((i < n - 1) or (arr[n - 1] == key)):
        return(i)
    else:
        return None


print(sentinelSearch(trial_list, len(trial_list), 9))