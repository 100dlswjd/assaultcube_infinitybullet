a = b'\xc81p\x00'

a = int.from_bytes(a,"little")

print(hex(a))