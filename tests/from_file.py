import os
import unittest
from jeml import from_string, from_file, to_string


class JEMLParsing(unittest.TestCase):
    def setUp(self):
        if "tests" not in os.getcwd():
            os.chdir(os.getcwd() + "/tests/")

    def test_file_people(self):
        file_string = from_file('files/people.jeml')
        self.assertEqual(file_string, {'person1': {'name': 'Judah'}, 'person2':{'name': 'Jim'}, 'person3': {'name': 'Kate'}})

    def test_file_realistic(self):
        file_string = from_file('files/realistic.jeml')
        self.assertEqual(file_string['package']['name'], 'project name')
        self.assertEqual(file_string['package']['version'], '1.0.0')
        self.assertEqual(file_string['package']['authors'][0], 'foo <foo@example.com>')
        self.assertEqual(file_string['package']['homepage'], 'https://github.com/foo/bar')
        self.assertEqual(file_string['package']['description'], 'Lorem ipsum dolor sit amet')
        self.assertEqual(file_string['package']['full-description'], 'Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet')
        self.assertEqual(file_string['package']['license'], 'MIT')
        self.assertEqual(file_string['package']['public'], True)
        self.assertEqual(file_string['package']['keywords'][1], 'bar')
        self.assertEqual(file_string['package']['dependencies_a'][2], 'bar==x.y.z')
        self.assertEqual(file_string['package']['dependencies_b']['jeml']['version'], '>=x.y.z')
        self.assertEqual(file_string['package']['include'][1], 'docs/**/*.md')
        self.assertEqual(file_string['package']['exclude'][0], '.git*')

        self.assertEqual(file_string['development']['debug'], True)
        self.assertEqual(file_string['development']['opt-level'], 0)
        self.assertEqual(file_string['development']['flags'], ['foo', 'bar', 'baz'])

        self.assertEqual(file_string['release']['debug'], False)
        self.assertEqual(file_string['release']['opt-level'], 3)
        self.assertEqual(file_string['release']['flags'], ['foo', 'bar', 'baz'])



if __name__ == '__main__':
    unittest.main(verbosity=2)
