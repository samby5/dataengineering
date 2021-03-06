def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command in ['add','remove'] and location in ['beginning','end']:
        if command == 'add':
            if location == 'beginning':
                lst.insert(0,value)
                print(lst)
            else:
                lst.insert(len(lst),value)
                return(lst)
        else:
            if location == 'beginning':
                return(lst.pop())
                #del(lst[0])
                print(lst)
            else:
                return(lst.pop(0))
                #del(lst[-1])
                print(lst)
    else:
        return None


lst = [1, 2, 3]
list_manipulation(lst, 'add', 'beginning', 20)
print(list_manipulation(lst, 'add', 'end', 30))
print(lst)
print(list_manipulation(lst, 'foo', 'end'))
print(list_manipulation(lst, 'add', 'dunno'))
print(list_manipulation(lst, 'remove', 'beginning'))
print(lst)
print(list_manipulation(lst, 'remove', 'end'))
print(lst)

