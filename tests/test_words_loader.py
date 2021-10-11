from randomit.words_loader import WordsLoader


def test_load_words_return_type():
    random_words = WordsLoader().load_random_words()

    assert isinstance(random_words, list)
    assert isinstance(random_words[0], str)
    assert type(random_words) != int
    assert type(random_words) != dict
    assert len(random_words) != 0


def test_load_name_words_returns():
    name_words = WordsLoader().load_name_words()

    assert isinstance(name_words, list)
    assert isinstance(name_words[0], str)
    assert type(name_words) != int
    assert type(name_words) != dict
    assert len(name_words) != 0


def test_load_surname_words_returns():
    surname_words = WordsLoader().load_surname_words()

    assert isinstance(surname_words, list)
    assert isinstance(surname_words[0], str)
    assert type(surname_words) != int
    assert type(surname_words) != dict
    assert len(surname_words) != 0
