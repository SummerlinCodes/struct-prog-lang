 import re 

# Define patterns for tokens 
patterns = [
    [r"\d+", "number"],
    [r"\+", "+"],
    ## adding minus , multiplication, and division
    ## ****** make sure to add these *******
    [r"\-", "-"],
    [r"\*", "*"],
    [r"\/", "/"],
    [r"\(", "("],
    [r"\)", ")"],
    [r"\s+", "whitespace"], 
    [r".", "error"] ## what does dot stand for?  It stands for anything ***
]

for pattern in patterns: 
    patterns[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        for pattern, tag in patterns:
            # allows the matching of two things at once (multiple assignment)
            match = pattern.match(characters, position) 
            if match: 
                break
        assert match 
        # (process errors)
        if tag == "error":
            raise Exception("Syntax error")
        token = {
            "tag":tag, 
            "position":position,
            "value":match.group(0) # means give me the content of the first group that matches this
        }
        if token["tag"] == "number": 
            token["value"] = int(token["value"])
        if token["tag"] != "whitespace":
            tokens.append(token) # saves token
        # what is the next step?  Need to update position for the next match
        position = match.end() # gives the next position
    # append end-of-stream marker
    tokens.append({ ##### Need to fix ####### *************
        "tag":None,
        "value":None,
        "position":position
    })
    return tokens

def test_simple_token(): 
    print("test simple token")
    examples = "+-*/()"
    for example in examples:
        t = tokenize(example)[0]
        assert t["tag"] == example # what kind of token is it? 
                                # means what they want from the tag == just the character
        assert t["position"] == 0 # where you found it
        assert t["value"] == example # what does it contain
def test_number_token():
    print("test number token")
    for s in ["1", "11"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0] ["tag"] == "number" 
        assert t[0] == int(s)
    
def test_multiple_tokens(): 
    print("test multiple tokens")
    tokens = tokenize ("1+2")
    assert tokens == [{'tag': }] ### grab results from terminal and paste *******

def test_whitespace(): 
    print("test white space")
    tokens = tokenize("1+2")
    assert tokens == [{'tag': }] ### same as above *****

def test_error(): 
    print("test error")
    try:
        t = tokenize("$1+2")
        assert False, "Should have raised an error for invalid character"
    except Exception as e: 
        assert "Syntax error" in str(e), f"Unexpected exception: {e}"

if __name__ == "__main__":
    test_simple_token()
    test_number_token()
    test_multiple_tokens()
    test_whitespace()
    test_error()