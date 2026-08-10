# Easy File Manager

Working with files is something you'll do in many Python projects. Whether you're checking if a file exists, creating files, reading their contents, renaming them, or making backups, `easy_file_manager` provides simple helpers that make common file operations easy to read and understand.

## A small real-world example

Imagine you're working on a project where you need to create a text file, add some information to it, read its contents, and then create a backup.

```python
from py_simple import (
    make_blank_file,
    add_a_line,
    read_file_to_list,
    copy_file,
)

make_blank_file("notes", "txt")
add_a_line("notes.txt", "My first project")
add_a_line("notes.txt", "Learning Python")

lines = read_file_to_list("notes.txt")
print(lines)

copy_file("notes.txt", "notes_backup.txt")
```

Example output:

```text
['My first project', 'Learning Python']
```

## What happened?

`make_blank_file()` creates a new empty file using one of the supported extensions: `txt`, `md`, `log`, or `csv`.

`add_a_line()` adds a new line to an existing file. If the file doesn't exist, it creates it automatically.

`read_file_to_list()` reads the file and returns its lines as a list.

`copy_file()` creates a copy of a file at another location or under another name without overwriting an existing file.

You can also check, rename, remove, or list files:

```python
from py_simple import (
    is_file_there,
    rename_file,
    list_files,
    remove_file,
)

if is_file_there("notes.txt"):
    print("The file exists.")

print(list_files("txt"))

rename_file("notes.txt", "project_notes.txt")

remove_file("project_notes.txt")
```

Example output:

```text
The file exists.
['notes.txt']
```

## Why use these helpers?

Instead of repeatedly writing `os.path.isfile()`, `open()`, `os.rename()`, `os.remove()`, and `shutil.copy2()`, you can simply write:

```python
if is_file_there("notes.txt"):
    add_a_line("notes.txt", "New information")

copy_file("notes.txt", "notes_backup.txt")
```

These helpers keep file management simple, readable, and beginner-friendly while providing useful tools for creating, reading, modifying, copying, renaming, removing, and listing common file types.