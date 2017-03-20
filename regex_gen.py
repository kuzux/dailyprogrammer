# challenge 306 [hard]
# https://www.reddit.com/r/dailyprogrammer/comments/5zxebw/20170317_challenge_306_hard_generate_strings_to/

import sys

class Char(object):
    def __init__(self, char):
        self.char = char
    def generate(self):
        return self.char
        
class Plus(object):
    def __init__(self, char):
        self.char = char
    def generate(self):
        return self.char.generate()

class Star(object):
    def __init__(self, char):
        self.char = char
    def generate(self):
        return ""

class Dash(object):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
    def generate(self):
        return self.c1

class Brace(object):
    def __init__(self):
        self.chars = []
    def generate(self):
        return self.chars[0].generate()

class Any(object):
    def __init__(self):
        pass
    def generate(self):
        return "a"

def parse(regex):
    res = []
    state = "start"
    prev = ""

    # a fsm with states="start", "brace", "dash", "backspace"

    for c in regex:
        if state == "backspace":
            state = prev
            if state == "brace":
                res[-1].chars[-1] = Char(res[-1].chars[-1].char)
            else:
                res[-1] = Char(res[-1].char)
        elif c == "\\":
            prev = state
            state = "backspace"
        elif c == "[":
            if state != "start":
                print "syntax error"
            state = "brace"
            res.append(Brace())
        elif c == "]":
            if state != "brace":
                print "syntax error"
            state = "start"
        elif c == "-":
            if state != "brace":
                print "syntax error"
            prev = state
            state = "dash"
        elif c == "*":
            if state == "brace":
                res[-1].chars[-1] = Star(res[-1].chars[-1])
            else:
                res[-1] = Star(res[-1])
        elif c == "+":
            if state == "brace":
                res[-1].chars[-1] = Plus(res[-1].chars[-1])
            else:
                res[-1] = Plus(res[-1])
        else:
            target = None 

            if state == "dash":
                res[-1].chars[-1] = Dash(res[-1].chars[-1].char, c)
                state = prev
                continue 
            elif state == "brace":
                target = res[-1].chars
            else:
                # we have to be in the start state
                target = res
            
            if c == ".":
                target.append(Any())
            else:
                target.append(Char(c))

    return res

for line in sys.stdin:
    r = parse(line.rstrip())
    cs = map(lambda c: c.generate(), r)
    res = "".join(cs)
    print res
