from .primitives import *
from .combiners import combine, sequence
from .parser import Parser

ParserOutput = tuple[object, str] | None
'''The output of a parser function (in this module encapsulated by the Parser class)
which takes in a string and returns this type.'''