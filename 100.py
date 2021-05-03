import base64

class SubstitutionCipher:
    def __init__(self, pt, ct):
        self.encode_trans = str.maketrans(pt, ct)
        self.decode_trans = str.maketrans(ct, pt)

    def encode(self, s):
        return s.translate(self.encode_trans)

    def decode(self, s):
        return s.translate(self.decode_trans)


def Base32Decode(string):
        text = "ph2eifo3n5utg1j8d94qrvbmk0sal76c"
        restring = ""
        datalen = len(string) / 8 * 5
        num = 0
        ib = 0;
        if len(string) < 3:
                restring = chr(text.find(string[0]) | text.find(string[1]) << 5 & 255)
                return restring

        k = text.find(string[0]) | (text.find(string[1]) << 5)
        j = 10
        index = 2
        for i in range(int(datalen)):
                restring += chr(k & 255)
                k = k >> 8
                j -= 8
                while( j < 8 and index < len(string)):
                        k |= (text.find(string[index]) << j)
                        index += 1
                        j += 5

        return restring








DGABase32Cipher = SubstitutionCipher(
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567", # Base32
  "ph2eifo3n5utg1j8d94qrvbmk0sal76c", # RedDrip7
)

sample1 = "mudofi75f4tjvh" # from bambenek drop
sample1Deciphered = DGABase32Cipher.decode(sample1)
print(sample1Deciphered)

# I'm saving you some time and padding this for you,
# so b32decode won't complain about incorrect padding.
# You're welcome.
sample1Padding = "A="
print(base64.b32decode(sample1Deciphered + sample1Padding))



print(Base32Decode('mudofi75f4tjvh'))
