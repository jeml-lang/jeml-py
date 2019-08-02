import unittest
from jeml import from_string, from_file, to_string

class JEMLParsing(unittest.TestCase):
    def test_basic_string_parse(self):
        jeml_string = 'string_map { _val "value" }'
        self.assertEqual(from_string(jeml_string),
                {'string_map':{'_val':'value'}})


    def test_basic_string_number(self):
        jeml_string_int = 'map_with_int {_val 123 }'
        jeml_string_float = 'map_with_float { _val 1.23}'
        jeml_string_int_and_float = 'map_with_float_and_int {_val1 5 _val2 3.55}'

        self.assertEqual(from_string(jeml_string_int),
                {'map_with_int':{'_val':123}})
        self.assertEqual(from_string(jeml_string_float),
                {'map_with_float':{'_val':1.23}})
        self.assertEqual(from_string(jeml_string_int_and_float),
                {'map_with_float_and_int':{'_val1':5,'_val2':3.55}})


    def test_basic_string_ml(self):
        jeml_string_literal_singleline = '''
        ml_string {
            _val1 """Lorem ipsum dolor sit amet"""
        }'''
        jeml_string_mline = '''
        map_with_ml_string {
            _val """Lorem ipsum dolor
            sit amet"""
        }'''
        jeml_string_multi_mline = '''
        map_with_multiple_ml_strings {
            _val1 """Lorem ipsum dolor
            sit amet"""
            _val2 """Lorem ipsum dolor
            sit amet"""
        }'''

        self.assertEqual(from_string(jeml_string_literal_singleline),
                {'ml_string':{'_val1':"""Lorem ipsum dolor sit amet"""}})
        self.assertEqual(from_string(jeml_string_mline),
                {'map_with_ml_string':{'_val':"""Lorem ipsum dolor
            sit amet"""}})
        self.assertEqual(from_string(jeml_string_multi_mline),
                {'map_with_multiple_ml_strings': {'_val1':"""Lorem ipsum dolor
            sit amet""", '_val2':"""Lorem ipsum dolor
            sit amet"""}})


    def test_basic_string_complex(self):
        jeml_string_binary = 'map_with_binary { _val 0b0001 }'
        jeml_string_hex = 'map_with_hex { _val 0x45f }'
        jeml_string_octal = 'map_with_octal { _val 0o145 }'
        self.assertEqual(from_string(jeml_string_binary), {'map_with_binary':{'_val':'0b1'}}) # bin() when encoding seems truncates automatically
        self.assertEqual(from_string(jeml_string_hex), {'map_with_hex':{'_val':'0x45f'}})
        self.assertEqual(from_string(jeml_string_octal), {'map_with_octal':{'_val':'0o145'}})


    def test_string_nested_lists(self):
        jeml_string_nested_lists = 'nested_lists_map { _val1 [ [] [] [] [ [] ] ] _val2 [ [ [ [] ] ] ]}'
        jeml_string_nested_maps_and_lists = 'nested_lists_and_maps_map { _val1 [ [] ] _val2 { _sval2-1 [ [] [] [ [] ] ] } }'
        self.assertEqual(from_string(jeml_string_nested_lists), {'nested_lists_map':{'_val1':[[],[],[],[[]]],'_val2':[[[[]]]]}})
        self.assertEqual(from_string(jeml_string_nested_maps_and_lists), {'nested_lists_and_maps_map':{'_val1':[[]],'_val2':{'_sval2-1':[[],[],[[]]]}}})


    def test_string_nested_maps(self):
        jeml_string_nested_maps = 'nested_maps_map  { _val1  { _sval1-1  {}  _sval1-2  {} }   _val2   {}   _val3   { _sval3-1   { _ssval3-1-1 {}}}}'
        should_be_string = from_string(jeml_string_nested_maps)
        should_be_map = {'nested_maps_map': {'_val1': {'_sval1-1': {}, '_sval1-2': {}}, '_val2': {}, '_val3': {'_sval3-1': {'_ssval3-1-1': {}}}}}

        self.assertEqual(should_be_string['nested_maps_map']['_val1']['_sval1-1'], should_be_map['nested_maps_map']['_val1']['_sval1-1'])
        self.assertEqual(should_be_string['nested_maps_map']['_val2'], should_be_map['nested_maps_map']['_val2'])
        self.assertEqual(should_be_string, should_be_map)


    def test_string_multiple_maps(self):
        jeml_string_multiple_maps = '_val1 {} _val2 {} _val3 {}'
        self.assertEqual(from_string(jeml_string_multiple_maps), {'_val1': {}, '_val2': {}, '_val3': {}})


    def test_string_multiple_maps_and_submaps(self):
        jeml_string_multiple_maps_and_submaps = '_val1 { _sval1-1 {} } _val2 { _sval2-1 {} } _val3 { _sval3-1 {} }'
        self.assertEqual(from_string(jeml_string_multiple_maps_and_submaps), {'_val1': {'_sval1-1':{}}, '_val2': {'_sval2-1':{}}, '_val3': {'_sval3-1':{}}})


    def test_string_realistic(self):
        jeml_string_realistic = '''
_val1 {
    _sval1-1 "is _sval1-1"
    _sval1-2 100
    _sval1-3 3.14
    _sval1-4 {
        _ssval4-1 "is _ssval4-1"
        _ssval4-2 0x45
    }
}
_val2 {
    _sval2-1 "is _sval2-1"
    _sval2-2 200
    _sval2-3 1.69
    _sval2-4 {
        _ssval4-1 "is _ssval4-1"
        _ssval4-2 0b0001
    }
}'''
        should_be_dict = {
            '_val1': {'_sval1-1': 'is _sval1-1', '_sval1-2': 100, '_sval1-3': 3.14, '_sval1-4': { '_ssval4-1': 'is _ssval4-1', '_ssval4-2': '0x45' }},
            '_val2': {'_sval2-1': 'is _sval2-1', '_sval2-2': 200, '_sval2-3': 1.69, '_sval2-4': { '_ssval4-1': 'is _ssval4-1', '_ssval4-2': '0b1'}}}

        self.assertEqual(from_string(jeml_string_realistic), should_be_dict)


if __name__ == '__main__':
    unittest.main(verbosity=2)
