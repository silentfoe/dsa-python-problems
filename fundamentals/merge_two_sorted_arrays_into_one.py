# You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

# You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

# Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

# Examples (input -> output)
# * [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]

# my solution: 

def merge_arrays(arr1, arr2):
    
    answer = list(set(arr1 + arr2))
    
    return sorted(answer)


# clever solution found on the solutions page. (note: from https://docs.python.org/3/howto/sorting.html - "There is also a sorted() built-in function that builds a new sorted list from an iterable."

def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))