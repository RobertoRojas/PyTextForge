# PyTextForge

This module use **[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)** in order to generate files from a template, and create one CLI program to can use it in a terminal context getting the data as argument.

## Install

```Bash
python -m pip install -U pytextforge;
```

## How to use

These are some examples about the usage of this module. The idea is to integrate this tool with others in order to generate the document.

### Simple file

This example shows how to use a simple data in order to create an output.

#### Template

```Plain
This is a simple example:

- {{ a }}
```

#### Command

```Bash
python -m pytextforge --data "foo=This is a line" --template template.temp --output output.txt;
```

#### Output

```Plain
This is a simple example:

- This is a line
```

### JSON data

You can also send more complex inputs to this script using a JSON.

#### Template

```Plain
This is a simple example:

The list of elements is:

{% for element in foo.elements %}- {{ element }}
{% endfor %}
```

#### Command

```Bash
python -m pytextforge --json 'foo={"elements":[1,2,3,4,5]}' --template template.temp --output output.txt;
```

#### Output

```Plain
This is a simple example:

The list of elements is:

- 1
- 2
- 3
- 4
- 5

```

### Data from files

You can get the data from a file, it can be a plain text or a json format data.

#### Template

```Plain
In this example we got the follow files contents:

info.txt
-----
{{ infoplain }}
-----

info.json
-----
{{ infojson.info }}
-----
```

#### info.txt

```Plain
This is the info

from the plain file
```

#### info.json

```JSON
{"info": "This is the info from\nthe json file..."}
```

#### Command

```Bash
python -m pytextforge --data-file 'infoplain=info.txt' --json-file 'infojson=info.json' --template template.temp --output output.txt;
```

#### Output

```Plain
In this example we got the follow files contents:

info.txt
-----
This is the info

from the plain file
-----

info.json
-----
This is the info from
the json file...
-----
```

### Overwrite data

If you provide data with the same ID more than once, the argument of the left will be overwrited. If the data is empty, that argument will be ignored. This way, you can control overwrites.

#### Template

```Plain
This is a simple example:

The list of elements is:

{% for element in foo.elements %}- {{ element }}
{% endfor %}
```

#### Script

```Python
import json
import sys

def main():
    argument = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    if argument == 1:
        print(json.dumps({
            'elements': [0,9,8,7,6,5,4,3,2,1]
        }))
    else:
        print()

if __name__ == '__main__':
    main()
```

#### Command 1

```Bash
python -m pytextforge --json 'foo={"elements":[1,2,3,4,5]}' --json "foo=$(python script.py)" --template template.temp --output output.txt;
```

#### Output 1

```Plain
This is a simple example:

The list of elements is:

- 1
- 2
- 3
- 4
- 5

```
#### Command 2

```Bash
python -m pytextforge --json 'foo={"elements":[1,2,3,4,5]}' --json "foo=$(python script.py 1)" --template template.temp --output output.txt
```

#### Output 2

```Plain
This is a simple example:

The list of elements is:

- 0
- 9
- 8
- 7
- 6
- 5
- 4
- 3
- 2
- 1

```