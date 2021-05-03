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
            try:
                pt += DgaEscapeCipher.decode(ct[i+1])
            except:
                pt += ''
                #pt = '0' #TODO: is ths a correct assumption?
        elif ct[i-1] == '0':
            print('|i|')
        else:
            pt += DgaSubstitutionCipher.decode(ct[i])
        counter = counter + 1

    return pt

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






lineno = 0
for line in open("uniq-hostnames.txt"):
    line = line.strip()
    lineno += 1
    if lineno ==1 or lineno == 432 or lineno == 467:
        #print(lineno, line)
        data = line.split('.')[0][16:]
        print(Base32Decode(data))





