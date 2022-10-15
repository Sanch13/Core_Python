from string import capwords
import doctest

# def just_do_it(text: str) -> str:
#     """Capitalaze()"""
#     return text.capitalize()


def just_do_it(text: str) -> str:
    """
     >>> just_do_it('duck')
     'Duck'
     >>> just_do_it('a veritable flock of ducks')
     'A Veritable Flock Of Ducks'
     >>> just_do_it("I'm fresh out of ideas")
     "I'm Fresh Out Of Ideas"
     """
    return capwords(text)


if __name__ == '__main__':
    doctest.testmod()

