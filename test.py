import tool
import win32api
import win32file
import win32process
import win32con
import ctypes
import sys
import time


#PROCESS_ALL_ACCESS = 0x1F0FFF
PROCESS_ALL_ACCESS = win32con.PROCESS_ALL_ACCESS

OFFSET = 0x140

base_addr = tool.get_base_addr("ac_client")

"""
k32 = ctypes.WinDLL("kernel32")

OpenProcess = k32.OpenProcess
CloseHandle = k32.CloseHandle
ReadProcessMemory = k32.ReadProcessMemory
WriteProcessMemory = k32.WriteProcessMemory"""

#교체된 함수들
OpenProcess = win32api.OpenProcess
CloseHandle = win32file.CloseHandle
ReadProcessMemory = win32process.ReadProcessMemory
WriteProcessMemory = win32process.WriteProcessMemory


game_pid = tool.Getpid("ac_client")
print("pid : ",game_pid)

process = OpenProcess(PROCESS_ALL_ACCESS, False, game_pid)

if process:
    pass
else:
    print("프로세스 열다가 에러남")

bullet = 30
cur_bullet = 0
#target_addr = hex(base_addr + 0x0018AC00 + OFFSET)
pointer_start = base_addr + 0x0018AC00
print("타겟 주소 : ", pointer_start)


dos_sig = ReadProcessMemory(process, 0x400000, 2)
print(f"dos signiture(MZ) : {dos_sig}")


pointer_start : bytes = ReadProcessMemory(process, pointer_start, 4)
print("바로 읽어옴 : ",pointer_start)
pointer_start = int.from_bytes(pointer_start, "little")
target_val = ReadProcessMemory(process, pointer_start + OFFSET, 4)
while True:
    print(pointer_start)
    WriteProcessMemory(process, pointer_start + OFFSET, bullet.to_bytes(4,"little"))
target_val = int.from_bytes(target_val, "little")
print(f"current bullet : {target_val}")


#flag = CloseHandle(process)
CloseHandle(process)
"""if flag:
    pass
else:
    print("프로세스 못닫음 오류뜸")"""


error_code = ctypes.GetLastError()
print("에러 코드 : ",error_code)
