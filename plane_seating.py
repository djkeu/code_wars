import re
# ToDo: avoid repetition
    

def plane_seat(a):
    # No seat
    if re.search("[6][1-9].|[7-9][0-9].|.[IJ]", a):
        return "No Seat!!"

    # Back seats
    if re.search("[4-5][1-9][A-C]", a):
        return "Back-Left"
    elif re.search("[4-5][1-9][D-F]", a):
        return "Back-Middle"
    elif re.search("[4-5][1-9][GHK]", a):
        return "Back-Right"
    
    elif re.search("50[A-C]", a):
        return "Back-Left"
    elif re.search("50[D-F]", a):
        return "Back-Middle"
    elif re.search("50[GHK]", a):
        return "Back-Right"

    elif re.search("60[A-C]", a):
        return "Back-Left"
    elif re.search("60[D-F]", a):
        return "Back-Middle"
    elif re.search("60[GHK]", a):
        return "Back-Right"

    
    # Middle seats
    if re.search("[2-3][1-9][A-C]", a):
        return "Middle-Left"
    elif re.search("[2-3][1-9][D-F]", a):
        return "Middle-Middle"
    elif re.search("[2-3][1-9][GHK]", a):
        return "Middle-Right"

    elif re.search("40[A-C]", a):
        return "Middle-Left"
    elif re.search("40[D-F]", a):
        return "Middle-Middle"
    elif re.search("40[GHK]", a):
        return "Middle-Right"

    elif re.search("30[A-C]", a):
        return "Middle-Left"
    elif re.search("30[D-F]", a):
        return "Middle-Middle"
    elif re.search("30[GHK]", a):
        return "Middle-Right"


    # Front seats
    elif re.search("[1-9][A-C]", a):
        return "Front-Left"
    elif re.search("[1-9][D-F]", a):
        return "Front-Middle"
    elif re.search("[1-9][GHK]", a):
        return "Front-Right"

    elif re.search("20[A-C]", a):
        return "Front-Left"
    elif re.search("20[D-F]", a):
        return "Front-Middle"
    elif re.search("20[GHK]", a):
        return "Front-Right"

    elif re.search("10[A-C]", a):
        return "Front-Left"
    elif re.search("10[D-F]", a):
        return "Front-Middle"
    elif re.search("10[GHK]", a):
        return "Front-Right"
    

def test_plane_seat():
    assert plane_seat('2B') == 'Front-Left'
    assert plane_seat('20B') == 'Front-Left'
    assert plane_seat('58I') == 'No Seat!!'
    assert plane_seat('60D') == 'Back-Middle'
    assert plane_seat('17K') == 'Front-Right'


"""
Instructions:
Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.

To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.

the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:

'2B' would return 'Front-Left'.

If the number is over 60, or the letter is not valid, return 'No Seat!!'.
"""

# https://www.codewars.com/kata/57e8f757085f7c7d6300009a/train/python
