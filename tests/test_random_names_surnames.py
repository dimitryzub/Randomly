from randomit.random_names_surnames import NamesSurnames


def test_random_name():
    random_name = NamesSurnames().get_random_name()
    random_name_capitalize = NamesSurnames().get_random_name(capitalize=True)

    assert isinstance(random_name, str)
    assert type(random_name) != int
    assert type(random_name) != dict
    assert type(random_name) != list

    assert isinstance(random_name_capitalize, str)
    assert random_name_capitalize.istitle()
    assert type(random_name_capitalize) != int
    assert type(random_name_capitalize) != dict
    assert type(random_name_capitalize) != list


def test_random_names():
    random_names = NamesSurnames().get_random_names()
    random_names_C = NamesSurnames().get_random_names(capitalize=True)
    random_names_W = NamesSurnames().get_random_names(words_to_return=3)
    random_names_L = NamesSurnames().get_random_names(letter_starts_with='S')  # should lower to 's'

    random_names_WC = NamesSurnames().get_random_names(words_to_return=3, capitalize=True)
    random_names_LC = NamesSurnames().get_random_names(letter_starts_with='s', capitalize=True)
    random_names_LW = NamesSurnames().get_random_names(letter_starts_with='s', words_to_return=5)

    # should capitalize to 'A' + 3 words to return
    random_names_all_args = NamesSurnames().get_random_names(letter_starts_with='a', words_to_return=3, capitalize=True)

    assert isinstance(random_names, list)
    assert type(random_names) != dict
    assert isinstance(random_names[0], str)
    assert type(random_names[0]) != int

    assert random_names_C[0].istitle()
    assert isinstance(random_names_C, list)
    assert isinstance(random_names_C[0], str)

    assert len(random_names_W) == 3
    assert isinstance(random_names_W, list)
    assert isinstance(random_names_W[0], str)

    assert random_names_L[0].startswith('s')
    assert isinstance(random_names_L, list)
    assert isinstance(random_names_L[0], str)

    assert len(random_names_WC) == 3 and random_names_WC[0].istitle()

    assert random_names_LC[0].startswith('S')
    assert random_names_LC[0].istitle()
    assert random_names_LW[0].startswith('s')
    assert len(random_names_LW) == 5

    assert random_names_all_args[0].startswith('A')
    assert len(random_names_all_args) == 3
    assert random_names_all_args[0].istitle()
    assert isinstance(random_names_all_args, list)
    assert isinstance(random_names_all_args[0], str)


def test_random_surname():
    random_surname = NamesSurnames().get_random_surname()
    random_surname_capitalized = NamesSurnames().get_random_surname(capitalize=True)

    assert isinstance(random_surname, str)
    assert type(random_surname) != int
    assert type(random_surname) != dict
    assert type(random_surname) != list

    assert isinstance(random_surname_capitalized, str) and random_surname_capitalized.istitle()
    assert type(random_surname_capitalized) != int
    assert type(random_surname_capitalized) != dict
    assert type(random_surname_capitalized) != list


def test_random_surnames():
    random_surnames = NamesSurnames().get_random_surnames()
    random_surnames_C = NamesSurnames().get_random_surnames(capitalize=True)
    random_surnames_W = NamesSurnames().get_random_surnames(words_to_return=3)
    random_surnames_L = NamesSurnames().get_random_surnames(letter_starts_with='S')  # should lower to 's'

    random_surnames_WC = NamesSurnames().get_random_surnames(words_to_return=3, capitalize=True)
    random_surnames_LC = NamesSurnames().get_random_surnames(letter_starts_with='s', capitalize=True)
    random_surnames_LW = NamesSurnames().get_random_surnames(letter_starts_with='s', words_to_return=5)

    random_surnames_all_args = NamesSurnames().get_random_surnames(capitalize=True, words_to_return=3,
                                                                   letter_starts_with='a')

    assert random_surnames
    assert isinstance(random_surnames, list)
    assert isinstance(random_surnames[0], str)
    assert type(random_surnames[0]) != int

    assert random_surnames_C[0].istitle()
    assert isinstance(random_surnames_C, list)
    assert isinstance(random_surnames_C[0], str)

    assert len(random_surnames_W) == 3
    assert isinstance(random_surnames_W, list)
    assert isinstance(random_surnames_W[0], str)

    assert random_surnames_L[0].startswith('s')
    assert isinstance(random_surnames_L, list)
    assert isinstance(random_surnames_L[0], str)

    assert len(random_surnames_WC) == 3

    assert random_surnames_WC[0].istitle()
    assert random_surnames_LC[0].startswith('S')
    assert random_surnames_LC[0].istitle()
    assert random_surnames_LW[0].startswith('s')

    assert len(random_surnames_LW) == 5

    assert random_surnames_all_args[0].startswith('A')
    assert len(random_surnames_all_args) == 3
    assert random_surnames_all_args[0].istitle()
    assert isinstance(random_surnames_all_args, list)
    assert isinstance(random_surnames_all_args[0], str)


def test_random_name_surname():
    name_surname = NamesSurnames().get_random_name_surname()
    name_surname_C = NamesSurnames().get_random_name_surname(capitalize=True)

    assert isinstance(name_surname, str)
    assert type(name_surname) != int
    assert type(name_surname) != dict
    assert type(name_surname) != list
    assert name_surname is not None

    assert isinstance(name_surname_C, str)
    assert type(name_surname_C) != int
    assert type(name_surname_C) != dict
    assert type(name_surname_C) != list
    assert name_surname_C is not None
    assert name_surname_C[0].istitle()


def test_random_names_surnames():
    # Capital letters in variable names used to shorten
    # "words to return/capitalize/letter_starts_with" function arguments
    names_surnames = NamesSurnames().get_random_names_surnames()
    names_surnames_C = NamesSurnames().get_random_names_surnames(capitalize=True)
    names_surnames_N = NamesSurnames().get_random_names_surnames(names_to_return=5)
    names_surnames_NC = NamesSurnames().get_random_names_surnames(names_to_return=5, capitalize=True)

    assert isinstance(names_surnames, list)
    assert isinstance(names_surnames[0], str)
    assert type(names_surnames) != int
    assert type(names_surnames) != dict

    assert isinstance(names_surnames_C, list)
    assert isinstance(names_surnames_C[0], str)
    assert type(names_surnames_C) != int
    assert type(names_surnames_C) != dict
    assert names_surnames_C[0].istitle()

    assert isinstance(names_surnames_C, list)
    assert isinstance(names_surnames_C[0], str)
    assert type(names_surnames_C) != int
    assert type(names_surnames_C) != dict
    assert names_surnames_C[0].istitle()

    assert isinstance(names_surnames_N, list)
    assert isinstance(names_surnames_N[0], str)
    assert type(names_surnames_N) != int
    assert type(names_surnames_N) != dict
    assert len(names_surnames_N) == 5

    assert isinstance(names_surnames_NC, list)
    assert isinstance(names_surnames_NC[0], str)
    assert type(names_surnames_NC) != int
    assert type(names_surnames_NC) != dict
    assert len(names_surnames_NC) == 5
    assert names_surnames_NC[0].istitle()
