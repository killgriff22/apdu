from smartcard.util import *

print(40 * "-")
data = [59, 101, 0, 0, 156, 17, 1, 1, 3]
print("data = [59, 101, 0, 0, 156, 17, 1, 1, 3]")
print("toHexString(data) =", toHexString(data))
print("toHexString(data, COMMA) =", toHexString(data, COMMA))
print("toHexString(data, PACK) =", toHexString(data, PACK))
print("toHexString(data, HEX) =", toHexString(data, HEX))
print("toHexString(data, HEX | COMMA) =", toHexString(data, HEX | COMMA))
print("toHexString(data, HEX | UPPERCASE) =", toHexString(data, HEX | UPPERCASE))
print(
    "toHexString(data, HEX | UPPERCASE | COMMA) =",
    toHexString(data, HEX | UPPERCASE | COMMA),
)


print(40 * "-")
data = [0x3B, 0x65, 0x00, 0x00, 0x9C, 0x11, 0x01, 0x01, 0x03]
print("data = [ 0x3B, 0x65, 0x00, 0x00, 0x9C, 0x11, 0x01, 0x01, 0x03 ]")
print("toHexString(data, COMMA) =", toHexString(data, COMMA))
print("toHexString(data) =", toHexString(data))
print("toHexString(data, PACK) =", toHexString(data, PACK))
print("toHexString(data, HEX) =", toHexString(data, HEX))
print("toHexString(data, HEX | COMMA) =", toHexString(data, HEX | COMMA))
print("toHexString(data, HEX | UPPERCASE) =", toHexString(data, HEX | UPPERCASE))
print(
    "toHexString(data, HEX | UPPERCASE | COMMA) =",
    toHexString(data, HEX | UPPERCASE | COMMA),
)


import sys

if "win32" == sys.platform:
    print("press Enter to continue")
    sys.stdin.read(1)