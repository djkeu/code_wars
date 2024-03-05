from domain_from_url import domain_name


def test_domain_name():
    assert domain_name("http://www.google.com") == "google"
    assert domain_name("http://google.com") == "google"
    assert domain_name("www.google.com") == "google"
