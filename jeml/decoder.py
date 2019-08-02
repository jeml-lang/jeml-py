import sys

from antlr4 import *
from jeml.engine.jemlLexer import jemlLexer
from jeml.engine.jemlParser import jemlParser
from jeml.engine.jemlListener import jemlListener
from jeml.engine.jemlErrorHandler import ErrorHandler

def parse(input, filename=None):
    lexer     = jemlLexer(input)
    stream    = CommonTokenStream(lexer)
    parser    = jemlParser(stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    lexer.addErrorListener(ErrorHandler(filename))
    parser.addErrorListener(ErrorHandler(filename))

    AST       = parser.document()
    listener  = jemlListener()
    walker    = ParseTreeWalker()

    walker.walk(listener, AST)
    return listener.jeml

def from_string(string):
    input = InputStream(string)
    return parse(input)

def from_file(file):
    input = FileStream(file)
    return parse(input, file)

