## Jan 27th

## AST = Abstract Syntax Tree
Accept a string of tokens, return an AST expressed as stack of dictionaries
"""
"""
    simple_expression = number | "()" expression ")" | "-" simple_expression
    factor = simple_expression
    term = factor { "*"|"/" factor }
    arithmetic_expression = term { "+"|"-" term } # means plus or minus term
    expression = arithmetic_expression
"""