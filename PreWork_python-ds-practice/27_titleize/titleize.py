def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    nl = phrase.split(' ')
    o=[]
    for i in nl:
       o.append(i[0].upper()+i[1:].lower())
    print(' '.join(o))

titleize('oNLy cAPITALIZe fIRSt')
titleize('this is awesome')