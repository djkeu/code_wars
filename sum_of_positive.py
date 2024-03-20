def positive_sum(arr):
    positive_arr = []
    for n in arr:
        if n > 0:
            positive_arr.append(n)

    return sum(positive_arr)


def test_positive_sum():
    assert positive_sum([1,2,3,4,5]) == 15
    assert positive_sum([1,-2,3,4,5]) == 13
    assert positive_sum([-1,2,3,4,-5]) == 9
    

def test_empty_case():
    assert positive_sum([]) == 0     
    

# FixMe:  assert -6 == 0
def test_negative_case():
    assert positive_sum([-1,-2,-3,-4,-5]) == 0


# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
