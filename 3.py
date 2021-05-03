rotation = 4
pt_alphabet = "rq3gsalt6u1iyfzop572d49bnx8cvmkewhj"

ct_alphabet = "salt6u1iyfzop572d49bnx8cvmkewhjrq3g" # (pt_alphabet[rotation:] + pt_alphabet[:rotation]).upper()

encode_trans = str.maketrans(pt_alphabet, ct_alphabet)
decode_trans = str.maketrans(ct_alphabet, pt_alphabet)

def subst_encode(s):
    return s.translate(encode_trans)

def subst_decode(s):
    return s.translate(decode_trans)


print(subst_encode("hello friends"))



print(subst_decode("i3r eu116 usr e2hovt 5s2h ov6onr i3r 32f6r"))
