#Easy JSON

Working with JSON files is common when storing application settings, configuration data, or other structured information. 'easy_json' provides beginner-friendly helpers that make reading, updating, and formatting JSON files simple and easy to understand.

##A small real-world example

Imagine you're working with a configuration file for an application. You want to read the current settings, update the theme, and print the updated configuration in an easy-to-read format.

Suppose `config.json` contains:

```json
{
  "name": "My App",
  "theme": "light"
}
```
You can update and display the configuration like this:
```python
from py-simple import open_json, update_json, pretty_json

config=open_json("config.json")
print("Current theme: ", config["theme"])

update_json("config.json", {"theme": "dark"})

updated_config=open_json("config.json")
print(pretty_json(data=updated_config))
```

Example output:

```text
Current theme: light
{
  "name": "My App",
  "theme": "dark"
}
```

## What happened?

`open_json()` reads the contents of `config.json` and returns them as a dictionary.

`update_json()` updates the existing `"theme"` value from `"light"` to `"dark"` while keeping the other settings unchanged.

`pretty_json()` formats the updated configuration as an indented JSON string, making it easier to read.

## Why use these helpers?

Instead of manually opening JSON files, updating dictionaries, saving changes, and formatting the output yourself, you can use a few simple helper functions:

```python
config = open_json("config.json")
update_json("config.json", {"theme": "dark"})
config = open_json("config.json")
print(pretty_json(data=config))
```

These helpers keep common JSON file operations simple, readable, and beginner-friendly while reducing repetitive code.