import pytest
from pathlib import Path
from randomit.words_randomizer import Words

# test file for passing custom file to Words(file=FILE) object
TEST_FILE = Path(__file__).parent.parent.resolve() / "randomit" / "words_storage" / "cities_list.txt"


def test_available_themes():
    words_theme = Words().available_themes()

    assert isinstance(words_theme, list)
    assert len(words_theme) != 0

    for theme in words_theme:
        assert isinstance(theme, str)


def test_load_words():
    # when passing own file:
    assert isinstance(Words(file=TEST_FILE).randomizer(), list)
    for custom_word in Words(file=TEST_FILE).randomizer():
        assert isinstance(custom_word, str)

    # when passing built-in themes:
    assert isinstance(Words(theme='random words').randomizer(), list)
    for rand_word in Words(theme='random words').randomizer():
        assert isinstance(rand_word, str)

    assert len(Words(theme='random words').randomizer()) != 0

    assert isinstance(Words(theme='names').randomizer(), list)
    for name_word in Words(theme='names').randomizer():
        assert isinstance(name_word, str)

    assert len(Words(theme='names').randomizer()) != 0

    assert isinstance(Words(theme='surnames').randomizer(), list)
    for surname_word in Words(theme='surnames').randomizer():
        assert isinstance(surname_word, str)

    assert len(Words(theme='surnames').randomizer()) != 0

    assert isinstance(Words(theme='cities').randomizer(), list)
    for city_word in Words(theme='cities').randomizer():
        assert isinstance(city_word, str)

    assert len(Words(theme='cities').randomizer()) != 0

    assert isinstance(Words(theme='countries').randomizer(), list)
    for country_word in Words(theme='countries').randomizer():
        assert isinstance(country_word, str)

    assert isinstance(Words(theme='address').randomizer(), list)
    for address_word in Words(theme='address').randomizer():
        assert isinstance(address_word, str)

    assert len(Words(theme='countries').randomizer()) != 0

    # if theme field is empty -> raise an error
    with pytest.raises(ValueError) as no_theme_error:
        Words(theme='').load_words()
    assert "Apparently, no theme is specified. Call available_themes() function to see available themes." in str(
        no_theme_error.value)

    # if different theme -> raise an error
    with pytest.raises(ValueError) as value_error:
        Words(theme='lol').load_words()
    assert "No such build-in theme. Hover over a Words() object to see available themes. Or call available_themes() function." in str(
        value_error.value)


def test_randomize_to_get_one_word():
    # when Words() argument is empty -> defaults to random_words.txt
    assert isinstance(Words().randomizer(return_one_word=True), str)


def test_randomize_to_get_multiple_words():
    # Capital letters in variable names used to shorten
    # "words to return/capitalize/letter_starts_with" function arguments

    random_words = Words(theme='random words').randomizer()
    random_names_C = Words(theme='names').randomizer(capitalize=True)
    random_words_W = Words(theme='countries').randomizer(words_to_return=3)
    random_name_one_word = Words(theme='names').randomizer(return_one_word=True)
    random_words_L = Words(theme='random words').randomizer(letter_starts_with='ATM')
    random_words_LW = Words(theme='cities').randomizer(letter_starts_with='A', words_to_return=5)
    random_names_WC = Words(theme='surnames').randomizer(words_to_return=5, capitalize=True)
    random_names_CL = Words(theme='names').randomizer(capitalize=True, letter_starts_with='Y')
    random_name_capitalized_one_word = Words(theme='surnames').randomizer(capitalize=True, return_one_word=True)
    random_names_WCL = Words(theme='names').randomizer(words_to_return=5, capitalize=True, letter_starts_with='V')

    assert isinstance(random_words, list)
    for word in random_words:
        assert isinstance(word, str)

    assert len(random_words) != 0

    assert isinstance(random_names_C, list)
    for word_C in random_names_C:
        assert isinstance(word_C, str)
        assert word_C.istitle()

    assert isinstance(random_words_W, list)
    for word_W in random_words_W:
        assert isinstance(word_W, str)

    assert len(random_words_W) == 3
    assert len(random_words_W) != 0

    assert isinstance(random_name_one_word, str)

    assert isinstance(random_words_L, list)
    for word_L in random_words_L:
        assert isinstance(word_L, str)
        assert word_L.startswith('atm')

    assert isinstance(random_words_LW, list)
    for word_LW in random_words_LW:
        assert isinstance(word_LW, str)
        assert word_LW.startswith('a')

    assert len(random_words_LW) == 5
    assert len(random_words_LW) != 0

    assert isinstance(random_names_WC, list)
    for word_WC in random_names_WC:
        assert isinstance(word_WC, str)
        assert word_WC.istitle()

    assert len(random_names_WC) == 5

    assert isinstance(random_names_CL, list)
    for word_CL in random_names_CL:
        assert isinstance(word_CL, str)
        assert word_CL.istitle()
        assert word_CL.startswith('Y')

    assert isinstance(random_name_capitalized_one_word, str)
    assert random_name_capitalized_one_word.istitle()

    assert isinstance(random_names_WCL, list)
    for word_WCL in random_names_WCL:
        assert isinstance(word_WCL, str)
        assert word_WCL.istitle()
        assert word_WCL.startswith('V')

    assert len(random_names_WCL) == 5
