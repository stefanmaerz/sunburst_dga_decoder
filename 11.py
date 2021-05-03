# -- coding: utf8 --


c = "𓀀"
# Convert to bytes, add one, then convert back to a string!

print(ord(c)+1)
val = ord(c)+1

newchar = chr(val)




print(newchar)







'''
last =  bytes(c, encoding='utf8')[-1] + 1
last = last.to_bytes(1, "big")

first = bytes(c, encoding='utf8')[0:-2]




print( first + last)


answer = first + last

print( answer.decode('utf-8'))
'''

'''
print(bytes(c, encoding='utf8'))


answer = last + first

print(answer)


print(answer.to_bytes(4, "big"))'''
