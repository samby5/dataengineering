def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    print((parens.count('(')==parens.count(')')) and parens[0]=='(' and parens[-1]==')')

valid_parentheses("((())")
valid_parentheses("()")
valid_parentheses("()()")

