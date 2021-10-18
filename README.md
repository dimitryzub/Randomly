# Randomit 🎲

A Python library to generate random things.

![pypi package versions brought by shields.io](https://img.shields.io/pypi/pyversions/randomit)
![pypi package badge brought by Gemfury](https://badge.fury.io/py/randomit.svg)
![pypy month downloads brought by shields.io](https://img.shields.io/pypi/dm/randomit?color=gree)
![licence brought by shields.io](https://img.shields.io/github/license/dimitryzub/randomit?color=blue)

![twitter account brought by shield.io](https://img.shields.io/twitter/follow/DimitryZub?style=social)
![reddit account brought by shield.io](https://img.shields.io/reddit/user-karma/combined/zdmit?style=social)
![youtube account brought by shields.io](https://img.shields.io/youtube/channel/views/UClEr5pKL0gfo4uGVH4nWRYg?style=social)
___
Currently, `randomit` can generate a [random word(s)](https://github.com/dimitryzub/randomit#randomize-words) based on a given [theme](https://github.com/dimitryzub/randomit#look-for-available-built-in-themes), 
as well as [load your words files](https://github.com/dimitryzub/randomit#load-and-pass-your-files) to randomize them. 

To see what's coming next, see [open projects](https://github.com/dimitryzub/randomit/projects).

## 🕹️Usage

> *Words will always be different on each execution no matter what arguments being passed.*

### Randomize words

```python
from randomit.words_randomizer import Words

# return one word
Words().randomizer(return_one_word=True)
# cabinet
# bristlecone pine
# dim - bright

Words().randomizer()  # returns a list of 17k words
Words().randomizer(words_to_return=3)  # ['axis', 'overabundant', 'superuser']

Words().randomizer(letter_starts_with='A')  # returns all words that starts with letter "A" 
Words().randomizer(letter_starts_with='A', words_to_return=3)  # ['abandoned', 'able', 'absolute']
Words().randomizer(letter_starts_with='A', words_to_return=3, capitalize=True) # ['Apron', 'Ashes', 'Anvil']
```

### Look for available built-in themes

_If "**theme**" argument is not specified ➡ defaults to "**random words**"_.

```python
Words().available_themes()
# ['random words', 'names', 'surnames', 'cities', 'countries', 'address']
```

### Specify theme you want to get words from

```python
Words(theme='cities').randomizer() # pass available arguments
```

### Load and pass your file(s)
_Make sure all words are **lowercase**, and start on a **new line** (`\n`), otherwise it won't work._

```python
# call your words
Words(file=YOUR_FILE).randomizer(return_one_word=True, capitalize=True)

# Bazinga!
```

___

## 📡 Installation

```
$ pip install randomit
```

```
$ git clone https://github.com/dimitryzub/randomit.git
```

## 👾 Suggestions

If you have any suggestions or ideas what will be good to add, get involved in [discussions](https://github.com/dimitryzub/randomit/discussions) section.

## 🔬 Issues

For issues, visit [issues page](https://github.com/dimitryzub/randomit/issues) 🙃

Note for [replit.com](https://replit.com/) users. If you’re using `randomit` on replit, it will throw an error for no obvious for me reason. If you know how to fix it, please, let me know. 

Installing package locally via `pip` doesn’t produce such error as it should (_tested in Pycharm_).