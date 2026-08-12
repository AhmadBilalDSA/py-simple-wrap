# Easy Images

Working with images is something you'll often need in Python projects. Resizing, converting, rotating, and inspecting images are common operations that usually require several lines of Pillow code.

The `easy_images` module provides simple helpers that make these common image-processing tasks easy to use without writing the underlying logic yourself.

## A small real-world example

Imagine you're creating an application that needs to resize a profile picture, convert an image to another format, and inspect its dimensions.

```python
from py_simple import resize_image, convert_image, get_image_info

resize_image("profile.png", "profile_small.png", 320, 320)
convert_image("profile.png", "profile.jpg")

info = get_image_info("profile.png")

print(info)
```

Example output:

```text
{'width': 1920, 'height': 1080, 'format': 'PNG', 'mode': 'RGBA'}
```

## What happened?

`resize_image()` resizes an image to the width and height you provide and saves the result to the output path.

`convert_image()` converts an image to another format based on the output file extension, such as converting PNG to JPG.

`rotate_image()` rotates an image by the angle you provide and saves the rotated image.

`get_image_info()` returns basic information about an image, including its width, height, format, and mode.

For example:

```python
from py_simple import rotate_image

rotate_image("photo.jpg", "photo_rotated.jpg", 90)
```

You can also inspect an image without modifying it:

```python
from py_simple import get_image_info

info = get_image_info("photo.jpg")
print(info)
```

## The Py_simple Way

```python
from py_simple import resize_image, convert_image, rotate_image

resize_image("photo.jpg", "small.jpg", 320, 240)
convert_image("photo.png", "photo.jpg")
rotate_image("photo.jpg", "rotated.jpg", 90)
```

## The Traditional Way

Without `py_simple`, you would normally have to work directly with Pillow:

```python
from PIL import Image

with Image.open("photo.jpg") as img:
    img.resize((320, 240)).save("small.jpg")

with Image.open("photo.png") as img:
    img.convert("RGB").save("photo.jpg")

with Image.open("photo.jpg") as img:
    img.rotate(90, expand=True).save("rotated.jpg")
```

## Getting image information

`get_image_info()` returns a dictionary containing:

* `width` — Image width in pixels.
* `height` — Image height in pixels.
* `format` — Image format, such as `PNG` or `JPEG`.
* `mode` — Image color mode, such as `RGB` or `RGBA`.

```python
from py_simple import get_image_info

info = get_image_info("photo.jpg")
print(info)
```

Example output:

```text
{'width': 1920, 'height': 1080, 'format': 'JPEG', 'mode': 'RGB'}
```

## Error handling

The `easy_images` module provides `ImageProcessingError` to give image-related failures a consistent and easy-to-understand exception.

For example:

```python
from py_simple import get_image_info, ImageProcessingError

try:
    info = get_image_info("missing.jpg")
except ImageProcessingError as error:
    print(error)
```

This prevents errors from Pillow or the operating system from leaking directly into your application.

## Why use these helpers?

Instead of repeatedly writing Pillow code for common image operations, you can simply use:

```python
resize_image("photo.jpg", "small.jpg", 320, 240)
convert_image("photo.png", "photo.jpg")
rotate_image("photo.jpg", "rotated.jpg", 90)
info = get_image_info("photo.jpg")
```

These helpers keep common image-processing tasks simple, readable, and beginner-friendly while handling the underlying Pillow logic for you.
