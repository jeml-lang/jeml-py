import os
import unittest
from jeml import from_string, from_file, to_string

class JEMLParsing(unittest.TestCase):
    def setUp(self):
        if "tests" not in os.getcwd():
            os.chdir(os.getcwd() + "/tests/")


    def test_dict_basic(self):
        basic_dict = {'_val1': {'_val1-1': 1, '_val1-2': '_val1 string'}}
        basic_string = to_string(basic_dict)
        self.assertEqual(basic_string,
"""_val1 {
  _val1-1 1
  _val1-2 "_val1 string"
}""".strip())


    def test_dict_nested_maps(self):
        basic_dict_nested_maps = {'_val1': {'_val1-1': {'_val1-1-1': True},'_val1-2': {'_val1-2-1': {},'_val1-2-2': {}}}}
        basic_dict_nested_string = to_string(basic_dict_nested_maps)
        self.assertEqual(basic_dict_nested_string,
"""
_val1 {
  _val1-1 {
    _val1-1-1 true
  }
  _val1-2 {
    _val1-2-1 {}
    _val1-2-2 {}
  }
}""".strip())


    def test_dict_nested_list(self):
        basic_dict_nested_lists = {'_val1': { '_val1-1': [[], [], [], [], []], '_val1-2': [[[[]]]] } }
        basic_dict_nested_lists_string = to_string(basic_dict_nested_lists)
        self.assertEqual(basic_dict_nested_lists_string,
"""
_val1 {
  _val1-1 [[] [] [] [] []]
  _val1-2 [[[[]]]]
}
""".strip())


if __name__ == '__main__':
    unittest.main(verbosity=2)
