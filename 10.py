bambenek = [
    "02m6hcopd17p6h450gt3.appsync-api.us-west-2.avsvmcloud.com",
    "039n5tnndkhrfn5cun0y0sz02hij0b12.appsync-api.us-west-2.avsvmcloud.com",
    "043o9vacvthf0v95t81l.appsync-api.us-east-2.avsvmcloud.com",
    "04jrge684mgk4eq8m8adfg7.appsync-api.us-east-2.avsvmcloud.com",
    "04r0rndp6aom5fq5g6p1.appsync-api.us-west-2.avsvmcloud.com",
    "04spiistorug1jq5o6o0.appsync-api.us-west-2.avsvmcloud.com",
    "05q2sp0v4b5ramdf71l7.appsync-api.eu-west-1.avsvmcloud.com",
    "060mpkprgdk087ebcr1jov0te2h.appsync-api.us-east-1.avsvmcloud.com",
    "06o0865eliou4t0btvef0b12eu1.appsync-api.us-east-1.avsvmcloud.com",
    "07605jn8l36uranbtvef0b12eu1.appsync-api.us-east-1.avsvmcloud.com",
    "07q2aghbohp4bncce6vi0odsovertr2s.appsync-api.us-east-1.avsvmcloud.com",
    "07ttndaugjrj4pcbtvef0b12eu1.appsync-api.us-east-1.avsvmcloud.com",
    "08amtsejd02kobtb6h07ts2fd0b12eu1.appsync-api.eu-west-1.avsvmcloud.com",
]

# XXX Paste your decoder here
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
            print('')
        else:
            pt += DgaSubstitutionCipher.decode(ct[i])
        counter = counter + 1

    return pt


decodes = []
for domain in bambenek:
    dotparts = domain.split(".")
    encoded = dotparts[0] # XXX Correct this!
    encoded = encoded[16:]
    decoded = DgaSubstDecode(encoded)
    print(domain, decoded)
    decodes.append(decoded)

answer = decodes[7]

print(answer)











