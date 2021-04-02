def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    #return(phrase[::-1])
    a=[]
    nl = [a.insert(0,i) for i in phrase]
    print(''.join(a))
reverse_string('MISHIKA')
