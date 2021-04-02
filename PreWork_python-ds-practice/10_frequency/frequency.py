def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    f=0
    for i in lst:
       if i == search_term:
           f+=1
    return f
print(frequency([1, 4, 3, 4, 4], 4))
print(frequency([1, 4, 3], 7))