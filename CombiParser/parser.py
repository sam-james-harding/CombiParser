class Parser():
    '''A container for parsers, mostly to be used for when parsers must be used in another
    parser before they themselves are defined, such as in multiple recursive parsers that 
    reference each other. Simply create a ParserContainer, passing in None to the constructor
    (if no parser is defined yet), or a parser. The parser can later be set with the setParser
    method, even after another parser is defined in terms of the current one.
    The ParserContainer object itself should be passed in place of a parser.'''

    def __init__(self, parser=None):
        self.__parser = parser

    def setParser(self, parser):
        self.__parser = parser

    def __call__(self, inp: str):
        if self.__parser == None:
            raise ValueError("No internal parser set for Parser object to call.")

        return self.__parser(inp)

    def parse(self, inp: str):
        '''Applies the parser to the input, raising appropriate ValueErrors if necessary, and returning the parser output'''

        if self.__parser == None:
            raise ValueError("No internal parser set for Parser object to call.")

        result = self(inp)

        if result == None:
            raise ValueError("Input could not be successfully parsed")

        output, remaining = result

        if remaining != "":
            raise ValueError("Input could not be fully parsed")

        return output