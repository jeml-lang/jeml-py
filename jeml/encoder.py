import os
import sys


def to_string(input):
    encoder = JEMLEncoder(input)
    return encoder.traverse(encoder.input)


class JEMLEncoder():
    def __init__(self, _input=dict):
        self.input = _input
        self.indent = 0

    def tab(self):
        return ' ' * self.indent

    def traverse(self, item):
        return_value = ""

        for key, value in item.items():
            if isinstance(value, dict):
                return_value += self.tab()
                return_value += '%s {' % key
                self.indent  += 2
                inner_value = self.traverse(value)
                if len(inner_value) <= 1:
                    return_value += '}\n'
                    self.indent -= 2
                else:
                    return_value += '\n%s%s\n' % (self.tab(), inner_value.strip())
                    self.indent  -= 2
                    return_value += self.tab() + '}\n'
            elif isinstance(value, list):
                return_value += self.tab()
                return_value += '%s [' % key
                return_value += self.format_list(value)
                return_value += ']\n'
            elif isinstance(value, str):
                return_value += self.tab()
                if self.is_complex(value):
                    return_value += '%s %s\n' % (key, value)
                else:
                    if self.is_multiline_string(value) or key.endswith('!'):
                        return_value += '%s """%s"""\n' % (key, value)
                    else:
                        return_value += '%s "%s"\n' % (key, value)
            elif isinstance(value, (int, float)) and not isinstance(value, bool):
                return_value += self.tab()
                return_value += '%s %s\n' % (key, value)
            elif isinstance(value, bool):
                return_value += self.tab()
                if value == True:
                    return_value += '%s true\n' % key
                elif value == False:
                    return_value += '%s false\n' % key
                else:
                    print("ERROR IN BOOLEAN VALUE: ", value)
                    exit(1)
            else:
                print("ERROR UNEXPECTED VALUE: ", value)
                exit(1)

        return return_value.strip()


    # format_list uses an odd hack that involves turning lst into a dictionary so
    # traverse() can walk over it. We then strip any excess characters and remove
    # our fake key ('_') that persists after the walk.
    def format_list(self, lst):
        final = []
        for val in lst:
            final.append(self.traverse({'_': val}))

        return ' '.join(map(lambda v: v.replace('_', '').strip(), final))


    def is_multiline_string(self, string):
        if hasattr(string, 'multiline'):
            if string.multiline == True:
                return True
            else:
                return False

        if '\n' in string or '\t' in string:
            return True

        return False


    def is_complex(self, value):
        complex_prefixes = ('0x', '0b', '0o')
        if value.startswith(complex_prefixes):
            return True
        return False
