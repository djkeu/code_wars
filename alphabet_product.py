"""
Description kata:
I have four positive integers, A, B, C and D, where A < B < C < D. The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order. Your task is to return the value of D. 
"""

def alphabet(ns):
    sorted_list = sorted(ns)

    remove_products = []

    AxB = sorted_list[0] * sorted_list[1]
    remove_products.append(AxB)
    BxC = sorted_list[1] * sorted_list[2]
    #remove_products.append(BxC)
    CxD = sorted_list[2] * sorted_list[3]
    #remove_products.append(CxD)
    DxA = sorted_list[3] * sorted_list[0]
    remove_products.append(DxA)

    for item in sorted_list:
        if item in remove_products:
            sorted_list.remove(item)  #FIXME only one item should be removed from sorted_list

            # max product of D == CxD
            # min product of D == DxA



    return sorted_list[3]


test = alphabet([2, 6, 7, 3, 14, 35, 15, 5])  # 7
print(test)

test = alphabet([2, 3, 4, 1, 12, 6, 2, 4])  # 4  # 6 should be 4
print(test)
