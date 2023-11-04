def freq_counter(coll):
    # accepts a collection
    """Returns frequency counter mapping of coll."""

    counts = {}
    # initiate an empty dictionary

    for x in coll:

        counts[x] = counts.get(x, 0) + 1
        # set the value off x to 0 at first and then add one, 
        # if it occurs again in the loop, just add one

    return counts


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    return freq_counter(str(num1)) == freq_counter(str(num2))
