def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    return (max(set(nums), key=nums.count))

# The max() function can return the maximum value of the given data set.
#  The key argument with the count() method compares and returns
# the number of times each element is present in the data set.
# Therefore, the function max(set(list_name), key = list_name.count)
#  will return the element that occurs the maximum times in the given 
# list that is the required mode of the list.

