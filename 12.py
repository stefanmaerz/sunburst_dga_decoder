import base64


enc = b"777ESABAABSCOD76EAAE2ACZAAQAAPOYG3OA===="
answer = base64.b32decode(enc)

print(answer.decode('utf-16'))
