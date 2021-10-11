from randomit.words_randomizer import WordRandomizer


def test_randomize_to_get_one_word():
    random_word = WordRandomizer().randomize_to_get_one_word()

    assert isinstance(random_word, str)
    assert type(random_word) != dict or list or int
    assert random_word is not None


def test_randomize_to_get_multiple_words():
    random_words = WordRandomizer().randomize_to_get_multiple_words()
    random_words_with_param = WordRandomizer().randomize_to_get_multiple_words(words_to_return=3)

    assert isinstance(random_words, list)
    assert isinstance(random_words[0], str)
    assert type(random_words[0]) != int

    assert type(random_words) != dict or int
    assert len(random_words) != 0

    assert isinstance(random_words_with_param, list)
    assert isinstance(random_words_with_param[0], str)
    assert type(random_words_with_param[0]) != int

    assert type(random_words_with_param) != int or dict
    assert len(random_words_with_param) == 3
    assert len(random_words_with_param) != 0


def test_randomize_words_that_start_with():
    random_words_that_starts_with = WordRandomizer().randomize_words_that_start_with('ATM')
    random_words_that_starts_with_param = WordRandomizer().randomize_words_that_start_with('A', words_to_return=5)

    assert random_words_that_starts_with[0].startswith('atm')
    assert isinstance(random_words_that_starts_with, list)
    assert isinstance(random_words_that_starts_with[0], str)
    assert type(random_words_that_starts_with[0]) != int
    assert type(random_words_that_starts_with) != int or dict

    assert isinstance(random_words_that_starts_with_param, list)
    assert isinstance(random_words_that_starts_with_param[0], str)
    assert type(random_words_that_starts_with_param[0]) != int
    assert type(random_words_that_starts_with_param) != int or dict

    assert random_words_that_starts_with_param[0].startswith('a')
    assert len(random_words_that_starts_with_param) == 5
    assert len(random_words_that_starts_with_param) != 0


def test_randomize_name():
    random_name = WordRandomizer().randomize_name()
    random_name_capitalized = WordRandomizer().randomize_name(capitalize=True)

    assert isinstance(random_name, str)
    assert type(random_name) != int or list or dict

    assert isinstance(random_name_capitalized, str)
    assert type(random_name_capitalized) != int or list or dict
    assert random_name_capitalized.istitle()


def test_randomize_names():
    # Capital letters in variable names used to shorten
    # "words to return/capitalize/letter_starts_with" function arguments
    random_names = WordRandomizer().randomize_names()
    random_names_C = WordRandomizer().randomize_names(capitalize=True)
    random_names_W = WordRandomizer().randomize_names(words_to_return=7)
    random_names_L = WordRandomizer().randomize_names(letter_starts_with='H')

    random_names_WC = WordRandomizer().randomize_names(words_to_return=5, capitalize=True)
    random_names_WL = WordRandomizer().randomize_names(words_to_return=8, letter_starts_with='T')
    random_names_CL = WordRandomizer().randomize_names(capitalize=True, letter_starts_with='Y')
    random_names_WCL = WordRandomizer().randomize_names(words_to_return=5, capitalize=True, letter_starts_with='V')

    # TODO: move the duplicate code into a separate function
    assert isinstance(random_names, list)
    assert isinstance(random_names[0], str)
    assert type(random_names) != int or dict

    assert isinstance(random_names_C, list)
    assert isinstance(random_names_C[0], str)
    assert type(random_names_C) != int or dict
    assert random_names_C[0].istitle()

    assert isinstance(random_names_W, list)
    assert isinstance(random_names_W[0], str)
    assert type(random_names_W) != int or dict
    assert len(random_names_W) == 7

    assert isinstance(random_names_L, list)
    assert isinstance(random_names_L[0], str)
    assert type(random_names_L) != int or dict
    assert random_names_L[0].startswith('h')

    assert isinstance(random_names_WC, list)
    assert isinstance(random_names_WC[0], str)
    assert type(random_names_WC) != int or dict
    assert len(random_names_WC) == 5 and random_names_WC[0].istitle()

    assert isinstance(random_names_CL, list)
    assert isinstance(random_names_CL[0], str)
    assert type(random_names_CL) != int or dict
    assert random_names_CL[0].istitle() and random_names_CL[0].startswith('Y')

    assert isinstance(random_names_WL, list)
    assert isinstance(random_names_WL[0], str)
    assert type(random_names_WL) != int or dict

    assert isinstance(random_names_WCL, list)
    assert isinstance(random_names_WCL[0], str)
    assert type(random_names_WCL) != int or dict
    assert len(random_names_WCL) == 5 and random_names_WCL[0].startswith('V') and random_names_WCL[0].istitle()
