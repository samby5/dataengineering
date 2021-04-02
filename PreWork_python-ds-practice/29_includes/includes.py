def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if not isinstance(collection,(dict,set)):
        if start is not None:
            if sought in collection[start:]:
                print(True)
            else:
                print(False)
        else:
            if sought in collection:
                print(True)
            else:
                print(False)
    else:
        if isinstance(collection,set):
            print(sought in collection)
        if sought in collection.values():
                print(True)
        else:
            print(False)
includes([1, 2, 3], 1)
includes([1, 2, 3], 1, 2)
includes("hello", "o")
includes(('Elmo', 5, 'red'), 'red', 1)
includes({1, 2, 3}, 1)
#includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
includes({"apple": "red", "berry": "blue"}, "blue")
