# Generated from jeml.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jemlParser import jemlParser
else:
    from jemlParser import jemlParser

class jemlStr(str):
    '''
        A simple wrapper for str that allows us to differentiate between
        string types without forcing the user into an arbitrary/pointless
        naming convention.
    '''
    def __new__(cls, *args, **kwargs):
        new_string = str.__new__(cls, *args, **kwargs)
        new_string.multiline = False
        return new_string


class jemlListener(ParseTreeListener):
    def __init__(self):
        self.jeml = {}
        # maps
        self.current_key  = None
        self.current_map  = None
        self.previous_map = None
        self.root_map     = None
        # lists
        self.current_list   = None
        self.previous_list  = None
        self.root_list      = None
        self.in_list        = False

    def push(self, value):
        if self.in_list:
            self.current_list.append(value)
        else:
            self.current_map[self.current_key] = value

    # When entering a document, initialize any top-level maps
    def enterDocument(self, ctx:jemlParser.DocumentContext):
        for top_level_map in ctx.j_map():
            key = top_level_map.j_key().getText()
            self.jeml[key] = {}

    def enterJ_map(self, ctx:jemlParser.J_mapContext):
        key = ctx.j_key().getText()

        # If the key is already initialized, it's top level and we
        # should move on
        if key in self.jeml:
            self.root_map = key
            self.jeml[self.root_map] = {}
            self.current_map = self.jeml[self.root_map]
            self.previous_map = self.current_map
            return self.exitJ_map(ctx)

        # If we don't have a root map key, set the current key as the root
        if self.root_map is None:
            self.root_map = key
            self.jeml[self.root_map] = {}
            self.current_map = self.jeml[self.root_map]
            self.previous_map = self.current_map
        else:
            # Otherwise, push any values to the current map
            self.previous_map = self.current_map
            self.current_map[key] = {}
            self.current_map = self.current_map[key]

    def exitJ_map(self, ctx:jemlParser.J_mapContext):
        # If we're back at the top-level, swap to our root
        if self.current_map == self.previous_map:
            self.current_map = self.jeml[self.root_map]
            self.previous_map = self.jeml
        else:
            # Swap our current map with our previous so we can return to the top-level
            self.current_map = self.previous_map


    # Almost identical to what we're doing with maps, except we have to keep
    # track of  what list depth we're at
    def enterJ_list(self, ctx:jemlParser.J_listContext):
        self.in_list = True
        if self.root_list is None:
            self.current_map[self.current_key] = list()
            self.root_list = self.current_map[self.current_key]
            self.current_list = self.root_list
            self.previous_list = self.current_list
        else:
            self.previous_list = self.current_list
            self.current_list.append(list())
            self.current_list = self.current_list[-1]

    def exitJ_list(self, ctx:jemlParser.J_listContext):
        if self.current_list == self.root_list or self.current_list == self.previous_list:
            self.in_list = False
            self.root_list = None
            self.previous_list = None
            self.current_list = None
        else:
            self.current_list = self.previous_list

    def enterJ_key(self, ctx:jemlParser.J_keyContext):
        self.current_key = ctx.KEY().getText()

    # If we find a string, check if it's multi-line (info provided by the parser),
    # cast it into our custom string type and set the necessary flag
    def enterJ_string(self, ctx:jemlParser.J_stringContext):
        if ctx.STRING() is not None:
            string_val = jemlStr(ctx.STRING().getText().strip('"'))
            self.push(string_val)
        else:
            mstring_val = jemlStr(ctx.MULTILINE_STRING().getText().strip('"'))
            mstring_val.multiline = True
            self.push(mstring_val)


    def enterJ_bool(self, ctx:jemlParser.J_boolContext):
        bool_value = ctx.BOOLEAN().getText()
        if bool_value == 'true':
            self.push(True)
        elif bool_value == 'false':
            self.push(False)
        else:
            print(f'Unexpected boolean value. Wanted ("true", "false"), received: {bool_value}')


    def enterJ_decimal(self, ctx:jemlParser.J_decimalContext):
        decimal_value = float(ctx.DECIMAL().getText())
        self.push(decimal_value)

    def enterJ_integer(self, ctx:jemlParser.J_integerContext):
        integer_value = int(ctx.INTEGER().getText())
        self.push(integer_value)

    # All complex numbers are simplified into a more basic form. There's a chance
    # we might not want this type of behaviour
    def enterJ_octal(self, ctx:jemlParser.J_octalContext):
        octal_value = int(ctx.OCTAL_NUMBER().getText(), base=8)
        self.push(oct(octal_value))

    def enterJ_binary(self, ctx:jemlParser.J_binaryContext):
        binary_value = int(ctx.BINARY_NUMBER().getText(), base=2)
        self.push(bin(binary_value))

    def enterJ_hex(self, ctx:jemlParser.J_hexContext):
        hex_value = int(ctx.HEXIDECIMAL_NUMBER().getText(), base=16)
        self.push(hex(hex_value))

