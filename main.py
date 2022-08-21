import tool
import win32api
import ctypes
import sys

PROCESS_ALL_ACCESS = 0x1F0FFF
OFFSET = 0x140
bullet = 30
cur_bullet = 0
base_addr = tool.get_base_addr("ac_client")

k32 = ctypes.WinDLL("kernel32")

OpenProcess = k32.OpenProcess
CloseHandle = k32.CloseHandle
ReadProcessMemory = k32.ReadProcessMemory
WriteProcessMemory = k32.WriteProcessMemory

game_pid = tool.Getpid("ac_client")
print("pid : ",game_pid)

process = OpenProcess(PROCESS_ALL_ACCESS, False, game_pid)


if process:
    target_addr = hex(base_addr+0x0018AC00+OFFSET)

    print("base addr : ",  hex(base_addr))
    print("타겟 주소 : ",target_addr)

    #ReadProcessMemory(process, target_addr, cur_bullet, sys.getsizeof(cur_bullet), 0)
    #WriteProcessMemory(process, target_addr, bullet, sys.getsizeof(bullet), 0)

    ReadProcessMemory(process, 0x006D0A48, cur_bullet, sys.getsizeof(cur_bullet), 0)
    WriteProcessMemory(process, 0x006D0A48, bullet, sys.getsizeof(bullet), 0)

    flag = CloseHandle(process)
    if flag:
        pass
    else:
        print("프로세스 못닫음 오류뜸")
else:
    print("프로세스 열다가 에러남")

error_code = ctypes.GetLastError()
print("에러 코드 : ",error_code)




