import re

def domain_name(url):
    url = re.sub("([A-Za-z]*://)?(www*.)?(\.[A-Za-z]*)?(/[A-Za-z]*)?", "", url)
    #url = re.sub("[A-Za-z]*://", "", url)
    #url = re.sub("www*.", "", url)
    #url = re.sub("\.[A-Za-z]*", "", url)
    #url = re.sub("/[A-Za-z]*", "", url)

    print(url)

domain_name("http://www.google.com")
domain_name("www.google.com")
domain_name("http://google.com")
