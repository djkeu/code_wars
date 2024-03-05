import re


def domain_name(url):
    url = re.sub("([A-Za-z]*://)?(www*.)?(\\.[A-Za-z]*)?(/[A-Za-z\\?]*)?", "", url)
    #url = re.sub("[A-Za-z]*://", "", url)
    #url = re.sub("www*.", "", url)
    #url = re.sub("\.[A-Za-z]*", "", url)
    #url = re.sub("/[A-Za-z]*", "", url)

    return url


def test_domain_name():
    assert domain_name("http://www.google.com") == "google"
    assert domain_name("http://google.com") == "google"
    assert domain_name("www.google.com") == "google"
    assert domain_name("http://www.google.com/test.txt") == "google"
    assert domain_name("http://www.google.com/testen/") == "google"

    assert domain_name("http://www.youtube.com/watch?dsfdrjkdf") == "youtube"
