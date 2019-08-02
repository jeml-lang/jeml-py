import sys

from antlr4 import *
from antlr4.error.ErrorListener import *

def print_error(_type, line, column, msg, filename=None):
    error_string = f'{_type} Error'
    pos = f'[{line}:{column}]'
    pos_infile = f'in {filename} ' if filename else ''
    print(f'{error_string} @ {pos} {pos_infile}: {msg}', file=sys.stderr)

def print_position(input_stream, column, expected):
    received = input_stream[column+1]
    received_string = f'Received: {input_stream[int(column/2):column]} {input_stream[column]} {received}'
    expected_string = f'Expected: {input_stream[int(column/2):column]} {input_stream[column]} {expected}'
    print(received_string, file=sys.stderr)
    print(' ' * (len(received_string) - len(received) - 1), '^' * len(received))
    print(expected_string, file=sys.stderr)
    print(' ' * (len(expected_string) - len(expected) - 1), '^' * len(expected))

class ErrorHandler(ErrorListener):
    def __init__(self, fname=None):
        self.filename = fname

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print_error('Syntax', line, column, msg, filename=self.filename)
        # possible usage for this in the future
        # if hasattr(recognizer, 'getExpectedTokens'):
            # print_position(recognizer.getInputStream().getText(), column, recognizer.getExpectedTokens().toString(recognizer.literalNames, recognizer.symbolicNames))
        exit(-1)
