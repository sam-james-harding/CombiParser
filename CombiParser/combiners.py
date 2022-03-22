from .parser import Parser

ParserOutput = tuple[object, str] | None

def combine(*parsers: Parser) -> Parser:
    '''Takes a series of parsers, and returns one new parser,
    which will return the result of the first parser not to fail,
    or None if they all fail.'''

    def combinedParser(inp: str) -> ParserOutput:
        for parser in parsers:
            # get the result of each parser, if it isn't None, that's the result
            # otherwise try the next one, and fail (return None) if none of them succeed
            result = parser(inp)
            
            if result != None:
                return result

        return None

    return Parser(combinedParser)

def sequence(outputFunc, *parsers: tuple[Parser, bool]) -> Parser:
    '''Takes a function and a series of tuples of Parsers and booleans.
    True marks the parser's output should be kept, False marks it should be discarded.
    All output kept will be passed to the function. The function should take the same
    number of arguments as there are parsers whose output is kept. The return value
    of the function will be the output of the parser. If any parser fails, the 
    parser returned by this function will fail.'''
    def sequencedParser(inp: str) -> ParserOutput:
        outputs = []

        for parser, shouldKeepOutput in parsers:
            result: ParserOutput = parser(inp)

            if result == None: # if the current parser fails, this whole parser fails
                return None

            parserOutput, inp = result # if it didn't fail, set the input to the unconsumed characters

            if shouldKeepOutput:
                outputs.append(parserOutput) #if the output should be kept, append it to outputs

        computedOutput = outputFunc(*outputs) #pass the parser outputs that were kept into the function

        return computedOutput, inp # return the output computed by the function, and the unconsumed characters

    return Parser(sequencedParser)

def union(*parsers: Parser) -> Parser:
    '''Takes a series of parsers, and returns a parser which will only succeed
    if all of the parsers return the same result when applied to an input string.
    If it succeeds, it returns that same value, and if it fails, it returns None.'''

    def unionParser(inp: str) -> ParserOutput:
        outputs = [parser(inp) for parser in parsers]

        for output in outputs:
            if output != outputs[0]: # if all outputs are the same
                return None

        return outputs[0]

    return Parser(unionParser)