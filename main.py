import tool
import win32api
import win32process
import win32con
import ctypes

PROCESS_ALL_ACCESS = win32con.PROCESS_ALL_ACCESS

OFFSET = [0x140]

base_addr = tool.get_base_addr("ac_client")

OpenProcess = win32api.OpenProcess
CloseHandle = win32api.CloseHandle
ReadProcessMemory = win32process.ReadProcessMemory
WriteProcessMemory = win32process.WriteProcessMemory

process_pid = tool.Getpid("ac_client")

process = OpenProcess(PROCESS_ALL_ACCESS, False, process_pid)

if process:
    bullet = 100
    pointer_start = base_addr + 0x0018AC00
    print(pointer_start)
    pointer_start : bytes = ReadProcessMemory(process, pointer_start, 4)
    pointer_start = int.from_bytes(pointer_start, "little")
    print(pointer_start)
    for addr in OFFSET:
        if addr == OFFSET[-1]:
            pass
        else:
            pointer_start = ReadProcessMemory(process, pointer_start + addr, 4)
            pointer_start = int.from_bytes(pointer_start, "little")

    WriteProcessMemory(process, pointer_start + OFFSET[-1], bullet.to_bytes(4,"little"))

   
    CloseHandle(process)
else:
    print("프로세서 열지 못함")