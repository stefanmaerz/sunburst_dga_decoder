pt_alphabet = "abcdefghijklmnopqrstuvwxyz"
ct_alphabet = "ZGLEIYMAXDHROPKWTQNSCVUBJF"

encode_trans = str.maketrans(pt_alphabet, ct_alphabet)
decode_trans = str.maketrans(ct_alphabet, pt_alphabet)

def subst_encode(s):
    return s.translate(encode_trans)

def subst_decode(s):
    return s.translate(decode_trans)

print(subst_decode("PXLI MKXPM DCPXKQ AZLHIQ"))
print(subst_decode("PXLI MKXPM DCPXKQ AZLHIQ"))
