<div align="center">
<!-- Once you have a logo/wordmark image, this pair auto-swaps by GitHub theme:
![py-simple-wrap](docs/assets/logo-dark.png#gh-dark-mode-only)
![py-simple-wrap](docs/assets/logo-light.png#gh-light-mode-only)
-->
 
# py-simple-wrap
 
**Making Python feel like plain English.**
 
[![PyPI](https://img.shields.io/pypi/v/py-simple-wrap?style=flat-square&logo=pypi&logoColor=white&color=3775A9)](https://pypi.org/project/py-simple-wrap/)
[![Tests](https://img.shields.io/github/actions/workflow/status/sara-czasak/py-simple-wrap/tests.yml?style=flat-square&logo=github&label=tests)](https://github.com/sara-czasak/py-simple-wrap/actions/workflows/tests.yml)
[![Contributors](https://img.shields.io/badge/contributors-31-orange?style=flat-square)](CONTRIBUTORS.md)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](LICENSE.md)
 
</div>
<br>
py-simple-wrap is a beginner-friendly Python toolbox — simple, intuitive functions for common tasks, so you can build something fun before the syntax gets in the way.
 
```bash
pip install py-simple-wrap
```
 
```python
from py_simple import make_blank_file, miles_to_km, is_valid_email
 
make_blank_file("notes.txt")
print(miles_to_km(26.2))                    # 42.16...
print(is_valid_email("hello@example.com"))  # True
```
 
> Full walkthrough in [QUICKSTART.md](QUICKSTART.md), or browse the **[documentation site](https://sara-czasak.github.io/py-simple-wrap/docs/)**.
 
<br>
## 😰 → 😎 See the difference
 
**The traditional way**
```python
import requests
from bs4 import BeautifulSoup
 
try:
    response = requests.get('https://github.com', timeout=10)
    response.raise_for_status()
    page = BeautifulSoup(response.content, 'html.parser')
    title = page.title.string
except Exception as e:
    print("The site is down or address is invalid.")
```
 
**The py-simple-wrap way**
```python
from py_simple import get_page_title
 
print(get_page_title("https://github.com"))
```
 
<br>

## 📚 Documentation
 
<div align="center">

| <div style="width:350px">📦 **[Module reference](MODULES.md)**</div> | <div style="width:350px">🤝 **[Contributor hub](https://sara-czasak.github.io/py-simple-wrap/docs/contributor-hub/)**</div> | <div style="width:350px">🗺️ **[Contributors quest](https://sara-czasak.github.io/py-simple-wrap/quest/)**</div> |
|:--------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
|                      20+ modules, one line each                      |                                               start here — templates included                                               |                                        play your way through contributing                                        |
 
</div>
<details>
<summary><strong>22 modules at a glance</strong> (full detail in the module reference)</summary>
<br>

|              |             |            |
|:-------------|:------------|:-----------|
| 📂 Files     | 🕰️ Dates   | 🔢 Numbers |
| 📋 Lists     | 🔤 Strings  | ✂️ Text    |
| 🔄 Converter | ✅ Validator | 🌐 Web     |
| 🎨 Colors    | 🔄 Flow     | 📄 JSON    |
| 🔍 Regex     | ⚡ Async     | 🔑 Dict    |
| 🖼️ Images   | 🧮 Math     | 📊 Stats   |
| 📑 CSV       | 📈 Data viz | 🎮 Game    |
| 🎲 Generator |             |            |
 
</details>
<br>

## ⭐ If py-simple-wrap made something easier for you
 
Consider giving it a **star** — it helps other beginners find it. And if there's a function you wish existed, **fork it** and add it; this project grew because other people did exactly that.
 
<br>
<div align="center">

**[Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md) · [License](LICENSE.md)**
 
<sub>Built for beginners, grown by 30+ contributors ✨</sub>
 
</div>
