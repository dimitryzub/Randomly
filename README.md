# Randomit

A Python library to generate random things.

___
Currently, `randomit` can generate a [random word(s)](#randomize-words) based on a given [theme](#look-for-available-built-in-themes), 
as well as [load your words files](#load-and-pass-your-files-with-words) to randomize them. To see what's coming, see [open projects](https://github.com/dimitryzub/randomit/projects).

## Usage

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

```python
Words().available_themes()
# ['random words', 'names', 'surnames', 'cities', 'countries', 'address']
```

### Specify theme you want to get words from

```python
Words('cities').randomizer() # pass available arguments + other theme from available_themes()
```

### Load and pass your file(s) with words
_Make sure all words are **lowercase**, otherwise it won't work._

```python
# content of words_randomizer.py

# add your file at the top:
YOUR_FILE = Path(__file__).parent.resolve() / 'words_storage' / 'YOUR_LIST.txt'

# add a short name in Words() class __init__ function
def __init__(self, theme: str = 'YOUR THEME NAME' or 'ANOTHER THEME NAME'):
        self.theme = theme.lower().strip()

# pass file to load_words() function
def load_words(self) -> list[str]:
    if 'YOUR THEME NAME' in self.theme:
        with open(YOUR_FILE, 'r', encoding='utf-8') as YOUR_WORDS:
            return [YOUR_WORD.replace('\n', '') for YOUR_WORD in YOUR_WORDS]

# call your words
Words('YOUR THEME NAME').randomizer(return_one_word=True, capitalize=True)

# Bazinga! 
```

___

## Installation

```
$ pip install randomit
```

```
$ git clone https://github.com/dimitryzub/randomit.git
```

## Suggestions

If you have any suggestions or ideas what will be good to add, get involved in [discussions](https://github.com/dimitryzub/randomit/discussions) section.