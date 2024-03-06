def pig_it(text):
    words = text.split()
    new_words = ""

    for word in words:
        if word.isalpha():
            word = word[1:] + word[0] + "ay"
        new_words += word + " "

    return new_words.strip()


def test_pig_it():
    assert pig_it("Pig latin is cool") == "igPay atinlay siay oolcay"
    assert pig_it("Hello world !") == "elloHay orldway !"
    assert pig_it("This is my string") == "hisTay siay ymay tringsay"
