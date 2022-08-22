import win32api
import win32con

a = b'\xff\x08'


print(a)

a = int.from_bytes(a,"little")

print(a)

