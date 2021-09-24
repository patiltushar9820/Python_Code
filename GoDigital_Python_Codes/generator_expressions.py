#generator expressions
"""
    gen_exp=(x*x for x in range(10))
    >>> gen_exp
    <generator object <genexpr> at 0x000001E0A4CCBF90>
    >>> list(gen_exp)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>>
"""