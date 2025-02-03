## Jan 27th
from tokenizer import tokenize
"""
parser.py -- implement parser for simple expressions

## AST = Abstract Syntax Tree
Accept a string of tokens, return an AST expressed as stack of dictionaries
"""

"""
    factor = <number>
    term = factor { "*"|"\" factor }
    expression = term { "+"|"-" term }
"""

def parse_factor(tokens):
    token = tokens[0]
    if token["tag"] == "number":
        return {
            "tag":"number",
            "value":token["value"]
        }, tokens[1:] # returns all but the first token
    raise Exception(f"Unexpected token '{token['tag']}' at position
                    {token['position']}")    

def test_parse_factor(): 
    """
    factor = <number>
    """
    print("testing parse_factor()")
    for s in ["1", "22", "333"]: 
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        assert ast == {'tag': 'number', 'value': 1}
        assert tokens[0] ['tag'] == None
    #print(ast)
    #print(tokens)
    #exit(0)

def parse_term(tokens):
    """
    term = factor { "*"|"/" factor } # ******* how do we know if it's a factor? *******
    """
    node, tokens = parse_factor(tokens)
    while tokens[0] ["tag"] in ["*", "/"]:
        tag = tokens[0] ["tag"]
        tokens = tokens[1: ] # 1: is array slicing
        right_node, tokens = parse_factor(tokens)
        node = {"tag":tag, "left":node, "right":right_node} # left node is the original node
    return node, tokens

def test_parse_term():
    """
    term = factor { "*"|"/" factor }
    """
    print("testing parse_term()")

    tokens = tokenize("2*4")
    ast, tokens = parse_term(tokens)
    assert ast == {'tag': '*', 'left': { 'tag': 'number', 'value': 2}, 'right': {'tag': 'number' , 'value': 4}}
    tokens = tokenize("2*4/6")
    ast, tokens = parse_term(tokens)
    print(ast)
    exit(0)



def test_parse_expression ():
    tokens = tokenize("1")
    print(tokens)
    exit(0)

if __name__ == "__main__":
    test_parse_expression()
    test_parse_factor()
    test_parse_term()
