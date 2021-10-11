from randomit.random_words import Words


def test_get_random_word_func():
    random_word = Words().get_random_word()

    assert isinstance(random_word, str)
    assert type(random_word) != dict
    assert type(random_word) != list
    assert type(random_word) != int
    assert random_word is not None


def test_get_random_words_func():
    random_words = Words().get_random_words()
    random_words_with_param = Words().get_random_words(words_to_return=3)

    assert isinstance(random_words, list)
    assert isinstance(random_words[0], str)
    assert type(random_words[0]) != int

    assert type(random_words) != dict
    assert type(random_words) != int
    assert len(random_words) != 0

    assert isinstance(random_words_with_param, list)
    assert isinstance(random_words_with_param[0], str)
    assert type(random_words_with_param[0]) != int

    assert type(random_words_with_param) != int
    assert type(random_words_with_param) != dict
    assert len(random_words_with_param) == 3
    assert len(random_words_with_param) != 0


def test_random_words_that_starts_with_func():
    random_words_that_starts_with = Words().get_random_words_that_start_with('ATM')
    random_words_that_starts_with_param = Words().get_random_words_that_start_with('A', words_to_return=5)

    assert isinstance(random_words_that_starts_with, list)
    assert isinstance(random_words_that_starts_with[0], str)
    assert type(random_words_that_starts_with[0]) != int

    assert type(random_words_that_starts_with) != int
    assert type(random_words_that_starts_with) != dict

    assert isinstance(random_words_that_starts_with_param, list)
    assert isinstance(random_words_that_starts_with_param[0], str)
    assert type(random_words_that_starts_with_param[0]) != int

    assert type(random_words_that_starts_with_param) != int
    assert type(random_words_that_starts_with_param) != dict
    assert len(random_words_that_starts_with_param) == 5
    assert len(random_words_that_starts_with_param) != 0
