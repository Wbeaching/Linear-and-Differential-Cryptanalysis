from os import urandom
import string


def substitution(pt):
    assert len(pt) == 4
    for i in pt:
        assert i in string.hexdigits
    # Lookup Dictionary
    lookup_dict = {'0': 'e', '1': '4', '2': 'd', '3': '1', '4': '2', '5': 'f', '6': 'b', '7': '8', '8': '3', '9': 'a', 'a': '6', 'b': 'c', 'c': '5', 'd': '9', 'e': '0', 'f': '7'}
    # Replacement using Lookup Dictionary
    for i in range(len(pt)):
        pt = pt[:i] + lookup_dict[pt[i]] + pt[i+1:]
    return pt


def permutation(pt):
    assert len(pt) == 16
    for i in pt:
        assert i in string.hexdigits
    # Permutation Lookup
    plookup_dict = {0: 0, 1: 4, 2: 8, 3: 12, 4: 13, 5: 5, 6: 9, 7: 13, 8: 2, 9: 6, 10: 10, 11: 14, 12: 3, 13: 7, 14: 11, 15: 15}
    # Transposition of bit indices
    



if __name__ == '__main__':
    plaintext = raw_input("Enter the text you want to encrypt: ")