from typing import Annotated
from .globals import *
from .combiners import combine, sequence

def parseIf(cond: Callable[[str], bool]) -> Parser:
    '''Takes a function from a character to a boolean and returns a parser, which will
    parse one character that returns true when passed to that function.'''

    def newCharParser(inp: str) -> ParserOutput:
        if inp == "": # if input is empty there is nothing to parse
            return None
        elif cond(inp[0]): # if the first character matches the condition, parse it
            return (inp[0], inp[1:])
        else: # if the condition is failed, the parse fails
            return None

    return newCharParser

def parseNOrMore(parser: Parser, n: int) -> Parser:
    '''Takes a character parser, and a minimum number of iterations,
    and returns a string consisting of characters matching that
    character parser of at least length n'''

    def nOrMoreParser(inp: str) -> ParserOutput:
        nCollected = 0
        outputs = []

        while True:
            result = parser(inp)

            if result == None: break # end the loop if the parser fails

            parserOutput, inp = result #get parser output and set input to unconsumed characters
            outputs.append(parserOutput)
            nCollected += 1

        if nCollected < n: return None # if not enough could be collected, the parse fails

        return ''.join(outputs), inp # join output chars into string and return with unconsumed input

    return nOrMoreParser

some = lambda parser: parseNOrMore(parser, 1)
'''Parses a string of one or more occurences of characters accepted by the parser argument'''

many = lambda parser: parseNOrMore(parser, 0)
'''Parses a string of zero or more occurences of characters accepted by the parser argument'''

charParser = lambda c: parseIf(lambda char: char == c)
'''Takes a character, and returns a parser for one character equal to the argument'''

digitParser = parseIf(lambda char: char.isdigit())
'''Parses one digit character'''

natParser = sequence(
    lambda string: int(string),
    (some(digitParser), True)
)
'''Parses a natural number (i.e. a whole, non-negative number)'''

intParser = combine(
    sequence(
        lambda num: -num,
        (charParser("-"), False),
        (natParser, True)
    ),
    natParser
)
'''Parses an integer (i.e. a whole number)'''

whitespaceParser = many(
    parseIf(lambda char: char.isspace())
)
'''Parses any amount of whitespace (including none)'''