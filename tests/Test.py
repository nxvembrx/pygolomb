import binascii

import Golomb
from bitstring import BitArray

with open('QRNG', "rb") as f:
        s1 = f.read(1000000)
#         s2 = f.read(5)

c1 = BitArray(s1)
print(Golomb.Golomb(c1.bin))
# with open('res.txt', 'a') as the_file:
#     the_file.write(c1.bin)
# c2 = BitArray(s2)
# print(s)
# print(c1.bin)
# print(c2.bin)