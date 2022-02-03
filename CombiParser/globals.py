from typing import Callable, Optional

ParserOutput = Optional[tuple[object, str]]
Parser = Callable[[str], ParserOutput]

class ParserContainer():
    '''A container for parsers, mostly to be used for when parsers must be used in another
    parser before they themselves are defined, such as in multiple recursive parsers that 
    reference each other. Simply create a ParserContainer, passing in None to the constructor
    (if no parser is defined yet), or a parser. The parser can later be set with the setParser
    method, even after another parser is defined in terms of the current one.
    The ParserContainer object itself should be passed in place of a parser.'''

    def __init__(self, parser: Optional[Parser]):
        self.__parser = parser

    def setParser(self, parser):
        self.__parser = parser

    def __call__(self, inp: str):
        return self.__parser(inp)

def parse(parser: Parser | ParserContainer, inp: str):
    '''Applies the parser to the input, raising appropriate ValueErrors if necessary, and returning the parser output'''

    result = parser(inp)

    if result == None:
        raise ValueError("Input could not be successfully parsed")

    output, remaining = result

    if remaining != "":
        raise ValueError("Input could not be fully parsed")

    return output