def generate_hashtag(s):
    """
    # Done: It must start with a hashtag (#).
    # Done: All words must have their first letter capitalized.
    # ToDo: Capitalize result of the words have a lenght of 1
    # ToDo: If the final result is longer than 140 chars it must return false.
    # ToDo: If the input or the result is an empty string it must return false.
    """

    s_list = s.split()
    result = ""
    for item in s_list:
        item = item.strip().title()
        result += item

    return "#" + result


print(generate_hashtag("Codewars is niCe"))


def test_correct_hashtag_fixed():
    assert generate_hashtag('Codewars') == '#Codewars'
    assert generate_hashtag('Codewars      ') == '#Codewars'
    assert generate_hashtag('      Codewars') == '#Codewars'
    assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
    assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'
    assert generate_hashtag('CoDeWaRs is niCe') == '#CodewarsIsNice'
    assert generate_hashtag('c i n') == '#CIN'
    assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'
    
# "Should return False if the input is empty, or result is longer than 140 chars"
def test_false_hashtag_fixed():
    assert generate_hashtag('') == False
    assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False


"""
Instructions:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
