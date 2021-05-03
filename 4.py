class SubstitutionCipher:
    def __init__(self, pt, ct):
        self.encode_trans = str.maketrans(pt, ct)
        self.decode_trans = str.maketrans(ct, pt)

    def encode(self, s):
        return s.translate(self.encode_trans)

    def decode(self, s):
        return s.translate(self.decode_trans)

DgaSubstitutionCipher = SubstitutionCipher(
    "rq3gsalt6u1iyfzop572d49bnx8cvmkewhj",
    "salt6u1iyfzop572d49bnx8cvmkewhjrq3g",
)
DgaEscapeCipher = SubstitutionCipher(
    "0-_.0-_.0-_.0-_.0-_.0-_.0-_.0-_.0-_",
    "salt6u1iyfzop572d49bnx8cvmkewhjrq3g",
)

print(DgaEscapeCipher.decode("salt"))
print(DgaEscapeCipher.encode("0-_0-0"))

