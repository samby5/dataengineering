def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    n_lst = lst.copy()
    return([i for i in lst if n_lst.index(i)%2==0])


lst = [1, 2, 3, 4, 5]
print(remove_every_other(lst))


