def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    d={}
    for i in phrase:
        if i.lower() in ['a','e','i','o','u']:
            if(i.lower() not in d):
                d[i.lower()]=1
            else:
                d[i.lower()]+=1
    print(d)
vowel_count('HOW ARE YOU? i am great!')
