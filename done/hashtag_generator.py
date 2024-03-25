def generate_hashtag(s):
    if s == "":
        return False

    result = ""

    for item in s.split():
        result += item.strip().title()

    if len(result) < 140:
        return "#" + result
    else:
        return False


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


# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
