<h2 align="center">Randomly</h2>
<h6 align="center">Randomly is Python library to generate random things</h6>

<p align="center">
    <img src="https://images.pexels.com/photos/3844790/pexels-photo-3844790.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" alt="Abstract image from @didsss from Pexels" width="600"/>
</p>

<h3>Installation</h3>
```lang-none
git clone https://github.com/dimitryzub/Randomly.git
```

<h3>Usage</h3>
```python
from randomly import Words

# get random word
Words().get_random_word()
# cabinet
# bristlecone pine
# dim - bright

# get random words
Words().get_random_words()                   # returns a list of 17k words
Words().get_random_words(words_to_return=5)  # returns a list of 5 words

# get random words that starts with..
Words().get_random_words_that_starts_with('A')                      # returns all words that starts with letter "A" 
Words().get_random_words_that_starts_with('A', words_to_return=5)   # returns 5 words that starts with letter "A"
```

