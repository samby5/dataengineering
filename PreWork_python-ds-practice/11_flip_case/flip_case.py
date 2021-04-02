def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    l_st = to_swap.lower()
    u_st = to_swap.upper()
    p=''
    #return(phrase.replace(u_st,l_st).replace(to_swap,u_st))
    for i in phrase:
        if i == l_st or i==u_st:
            if i == l_st:
                p = p + i.upper()
            else:
                p = p + i.lower()
        else:
            p= p + i
    return(p)

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))