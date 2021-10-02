from randomly.random_word import Words

def test_get_random_word_func():
    random_word = Words().get_random_word()

    assert random_word
    assert isinstance(random_word, str)
    assert random_word is not None
    assert random_word != int

def test_get_random_words_func():
    random_words = Words().get_random_words()
    random_words_with_param = Words().get_random_words(words_to_return=3)

    assert isinstance(random_words, list)
    assert random_words != int
    assert len(random_words) != 0

    assert random_words_with_param != int
    assert isinstance(random_words_with_param, list)
    assert len(random_words_with_param) == 3
    assert len(random_words_with_param) != 0

def test_random_words_that_starts_with_func():
    random_words_that_starts_with = Words().get_random_words_that_starts_with('ATM')
    random_words_that_starts_with_param = Words().get_random_words_that_starts_with('A', words_to_return=5)

    assert isinstance(random_words_that_starts_with, list)
    assert random_words_that_starts_with != int

    assert isinstance(random_words_that_starts_with_param, list)
    assert random_words_that_starts_with_param != int
    assert len(random_words_that_starts_with_param) == 5




