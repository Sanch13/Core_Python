from Bill_Lubanovic_Introducing_Python.Ch_19_Be_a_Pythonista import cap_2
from nose.tools import eq_


def test_one_word():
    text = 'duck'
    result = cap_2.just_do_it(text)
    eq_(result, 'Duck')


def test_multiple_words():
    text = 'a veritable flock of ducks'
    result = cap_2.just_do_it(text)
    eq_(result, 'A Veritable Flock Of Ducks')


def test_words_with_apostrophes():
    text = "I'm fresh out of ideas"
    result = cap_2.just_do_it(text)
    eq_(result, "I'm Fresh Out Of Ideas")


def test_words_with_quotes():
    text = "\"You're despicable,\" said Daffy Duck"
    result = cap_2.just_do_it(text)
    eq_(result, "\"You're Despicable,\" Said Daffy Duck")

