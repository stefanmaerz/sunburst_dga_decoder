class SubstitutionCipher:
    def __init__(self, pt, ct):
        self.encode_trans = str.maketrans(pt, ct)
        self.decode_trans = str.maketrans(ct, pt)

    def encode(self, s):
        return s.translate(self.encode_trans)

    def decode(self, s):
        return s.translate(self.decode_trans)

EscapeAlphabet = "0-_."

DgaSubstitutionCipher = SubstitutionCipher(
    "rq3gsalt6u1iyfzop572d49bnx8cvmkewhj",
    "salt6u1iyfzop572d49bnx8cvmkewhjrq3g",
)
DgaEscapeCipher = SubstitutionCipher(
    "0-_.0-_.0-_.0-_.0-_.0-_.0-_.0-_.0-_",
    "salt6u1iyfzop572d49bnx8cvmkewhjrq3g",
)

def DgaSubstEncode(text):
    ct = ""
    for c in text:
        if c in EscapeAlphabet:
            ct += "0"
            ct += DgaEscapeCipher.encode(c)
        else:
            ct += DgaSubstitutionCipher.encode(c)
    return ct


def DgaSubstDecode(ct):
    counter = 0
    #print(ct)
    pt=''
    for i in range(len(ct)): # c in ct:
        #if c in DgaEscapeCipher.decode(EscapeAlphabet):
        #    pt += DgaEscapeCipher.decode(c)
        #print("C is", c)

        if ct[i] == '0':
            pt += DgaEscapeCipher.decode(ct[i+1])
        elif ct[i-1] == '0':
            print('')
        else:
            pt += DgaSubstitutionCipher.decode(ct[i])
        counter = counter + 1

    return pt

cipherText = DgaSubstEncode("hello_friend_20.")

print(cipherText)


print('k*********************skldjfsldjfkljsd')
print(DgaSubstDecode(cipherText))

print(DgaSubstDecode('p2f03non03u03t0q0qn03g2c0r'))

