
Randomly is Python library to generate random things


## Installation
Using pip:
```python
pip install randomit
```

Using Git clone:
```
git clone https://github.com/dimitryzub/randomit.git
```


## Usage

```python
from randomit import Words

# get random word
Words().get_random_word()
# cabinet
# bristlecone pine
# dim - bright

# get random words
Words().get_random_words()  # returns a list of 17k words
Words().get_random_words(words_to_return=3)  # ['axis', 'overabundant', 'superuser']

# get random words that starts with..
Words().get_random_words_that_starts_with('A')  # returns all words that starts with letter "A" 
Words().get_random_words_that_starts_with('A', words_to_return=3)  # ['abandoned', 'able', 'absolute']
```

