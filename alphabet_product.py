def alphabet(ns):
    """
    I have four positive integers, A, B, C and D, where A < B < C < D. The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order. Your task is to return the value of D.
    """

    sorted_list = sorted(ns)
    print(sorted_list)
    sorted_list.insert(7, sorted_list.pop(4))

    i = 0
    while i < len(sorted_list[:3]):
        if sorted_list[i] == sorted_list[i+1]:
            sorted_list.insert(i+3, sorted_list.pop(sorted_list[i+1]))
        i += 1

    print(sorted_list)

    remove_products = []

    AxB = sorted_list[0] * sorted_list[1]
    remove_products.append(AxB)
    BxC = sorted_list[1] * sorted_list[2]
    remove_products.append(BxC)
    CxD = sorted_list[2] * sorted_list[3]
    remove_products.append(CxD)
    DxA = sorted_list[3] * sorted_list[0]
    remove_products.append(DxA)

    for item in sorted_list:
        if item in remove_products:
            sorted_list.remove(item)

    return sorted_list[3]


def test_alphabet():
    assert alphabet([2, 6, 7, 3, 14, 35, 15, 5])  == 7
    assert alphabet([2, 3, 4, 1, 12, 6, 2, 4])  == 4

alphabet([2, 6, 7, 3, 14, 35, 15, 5])  # FixMe: should not be 6
# alphabet([2, 3, 4, 1, 12, 6, 2, 4])  # Done:
