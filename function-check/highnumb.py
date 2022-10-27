def maximum(x, y, z):
    """
    A function that takes three numbers and returns the largest of them
    """

    if (x >= y) and (x >= z):

        largest = x

    if (y >= x) and (y >= z):

        largest = y

    if (z >= x) and (z >= y):

        largest = z

    return largest
