def pig_it(text):
    """
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
    """
    # code


def test_pig_it():
    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert pig_it("Hello world !") == "elloHay orldway !"
    assert pig_it("This is my string") == "hisTay siay ymay tringsay"

