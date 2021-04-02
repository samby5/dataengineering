def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    d={}
    for i in phrase:
        if i in d.keys():
            d[i] +=1
        else:
            d.update({i:1})
    return(d)
#print(multiple_letter_count('Yay'))