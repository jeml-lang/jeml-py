# JEML (for Python)

A simple Python library for working with [JEML (Just Enough Markup Language)](https://github.com/jeml-lang/jeml)!

## Installation

Automatic:  
```shell
pip install jeml==1.0.1
```

Manual:  
```shell
git clone https://github.com/jeml-lang/jeml-py
cd jeml-py
python setup.py install
```

## Usage

The API exposes three functions:  
  * `jeml.from_string` - Takes a JEML string and returns a Python dictionary
  * `jeml.from_file` - Takes the filename of a JEML file and returns a Python dictionary
  * `jeml.to_string` - Takes a python dictionary and returns a valid JEML string


## Examples

### Parsing a JEML File

*JEML file*:  
```
  person {
    name "Judah"
    bio "Creator of the JEML specification :)"
  }
```

*Python*:  
```python
  import jeml

  parsed = jeml.from_file('file.jeml')

  print(parsed)
  # { 'person': {'name': 'Judah', 'bio': 'Creator of the JEML specification :)' } }
```


### Parsing a JEML String

```python
  import jeml

  jeml_string = '''
    package {
      name "New Project"
      version "1.0.0"
      authors [ "foo <foo@example.com>" "bar <bar@example.com>" ]
      # [..] rest of jeml string
    }
  '''

  parsed = jeml.from_string(jeml_string)

  print(parsed)
  # { 'package': {'name': 'New Project', 'version': '1.0.0', 'authors': ['foo <foo@example.com>', 'bar <bar@example.com>'] } }
```

### Parsing a Python Dictionary into JEML

```python
  import jeml

  python_dict = { 'package': {'name': 'New Project', 'version': '1.0.0', 'authors': ['foo <foo@example.com>', 'bar <bar@example.com>'] } }
  jeml_string = jeml.to_string(python_dict)

  print(jeml_string)
  # package {
  #   name "New Project"
  #   version "1.0.0"
  #   authors ["foo <foo@example.com>" "bar <bar@example.com>"]
  # }
```


## API Reference

|Name|Argument(s)|Return Value|
|----|-----------|------------|
|`jeml.from_file(filename)`|`filename` (str) - A valid path to a JEML file. | A dictionary (dict) containing the parsed data. |
|`jeml.from_string(string)`|`string` (str) - A string containing valid JEML. | A dictionary (dict) containing the parsed data. |
|`jeml.to_string(_dict)`|`_dict` (dict) - A Python dictionary. | A string (str) of properly formatted JEML. |


## Notes

- `jeml.to_string` inlines any empty maps. It also inlines any list (filled or empty)
- `jeml.to_string` uses `2` space character indentation. 


## License
[MIT](LICENSE)
