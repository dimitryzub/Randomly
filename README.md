Currently, it can get you [random word(s)](#get-random-words), [name(s) and surname(s)](#get-random-names-and-surnames)
and it can [load your words files](#load-and-pass-your-files) to randomize them.

Words will always be different on each execution no matter what arguments being passed.

## Usage

#### Get random words:

```python
from randomit.random_words import Words

Words().get_random_word()
# cabinet
# bristlecone pine
# dim - bright

Words().get_random_words()  # returns a list of 17k words
Words().get_random_words(words_to_return=3)  # ['axis', 'overabundant', 'superuser']

Words().get_random_words_that_start_with('A')  # returns all words that starts with letter "A" 
Words().get_random_words_that_start_with('A', words_to_return=3)  # ['abandoned', 'able', 'absolute']
```

#### Get random names and surnames:

```python
from randomit.random_names_surnames import NamesSurnames

# random name
NamesSurnames().get_random_name()  # eric
NamesSurnames().get_random_name(capitalize=True)  # Brian

# random surname
NamesSurnames().get_random_surname()  # hucksam
NamesSurnames().get_random_surname(capitalize=True)  # Birman

# random names
NamesSurnames().get_random_names()  # returns a list() of all names
NamesSurnames().get_random_names(words_to_return=3, capitalize=True)  # ['Deandre', 'Tadeo', 'Edwin']
NamesSurnames().get_random_names(words_to_return=3, capitalize=True, letter_starts_with='S')  # ['Soren', 'Salem', 'Santino']

# random surnames
NamesSurnames().get_random_surnames()  # returns a list() of all surnames
NamesSurnames().get_random_surnames(words_to_return=3, capitalize=True)  # ['Gilgren', 'Macculloch', 'Trewhitt']
NamesSurnames().get_random_surnames(words_to_return=3, capitalize=True, letter_starts_with='G')  # ['Gilhome', 'Gom', 'Gammell']

# random name surname pair
NamesSurnames().get_random_name_surname()  # darius bremner 
NamesSurnames().get_random_name_surname(capitalize=True)  # Darwin Wage

# random name surname pairs
NamesSurnames().get_random_names_surnames()  # returns a list() of all name surname pairs
NamesSurnames().get_random_names_surnames(names_to_return=3, capitalize=True)  # ['Van Janson', 'Kason Pulcher', 'Aaire Fairbrass']
```

### Load and pass your files

You can add your own `txt` file(s) and pass them to `randomizer()` function that will have the same arguments as in
examples above. _Words will always be different on each execution_.

Load your words:

```python
# content of words_loader.py

YOUR_FILE = Path(__file__).parent.resolve() / 'words_storage' / 'your_file.txt'


def load_your_words(self):
    with open(YOUR_WORDS_FILE, 'r') as your_words:
        return [your_word.replace('\n', '') for your_word in your_words]
```

Randomize your words:

```python
# content of words_randomizer.py

def randomizer(self, letter_starts_with: str = '', words_to_return: int = 0, capitalize: bool = False):
    your_words = WordsLoader().load_your_words()
    # other code will be present here
```

Call them (_assumes you created a new `.py` file in the same dir_):

```python
# content of your_file.py
from randomit.words_randomizer import WordRandomizer


class MyRandomWords(WordRandomizer):
    def get_my_random_words(self, letter_starts_with: str = '', words_to_return: int = 0, capitalize: bool = False):
        return MyRandomWords().randomizer(letter_starts_with=letter_starts_with, words_to_return=words_to_return, capitalize=capitalize)


# call it 
MyRandomWords().get_my_random_words(capitalize=True, words_to_return=3, letter_starts_with='S')
```

## Installation

```
$ pip install randomit
```

```
$ git clone https://github.com/dimitryzub/randomit.git
```
