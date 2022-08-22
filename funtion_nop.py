import tool
import win32api
import win32process
import win32con
import time
import ctypes
PY_SSIZE_T_CLEAN = int
PROCESS_ALL_ACCESS = win32con.PROCESS_ALL_ACCESS

base_addr = tool.get_base_addr("ac_client")

OpenProcess = win32api.OpenProcess
CloseHandle = win32api.CloseHandle
ReadProcessMemory = win32process.ReadProcessMemory
WriteProcessMemory = win32process.WriteProcessMemory

process_pid = tool.Getpid("ac_client")

process = OpenProcess(PROCESS_ALL_ACCESS, False, process_pid)

if process:
    funtion_addr = base_addr + 0xC73EF
    nop_code = b'\x90\x90'
    org_code : bytes = ReadProcessMemory(process, funtion_addr, 2)
    org_code = b'\xff\x08'
    print(org_code)
    flag = False
    #WriteProcessMemory(process, funtion_addr, nop_code)
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_F8) & 0x8000:
            flag = not flag
            if flag:
                WriteProcessMemory(process, funtion_addr, nop_code)
                test_code : bytes = ReadProcessMemory(process, funtion_addr, 2)
                print(nop_code)
                print(test_code)
                print(ctypes.GetLastError())
                print("적용")
            else:
                WriteProcessMemory(process, funtion_addr, org_code)
                test_code : bytes = ReadProcessMemory(process, funtion_addr, 2)
                print(org_code)
                print(test_code)
                print(ctypes.GetLastError())
                print("해제")
            time.sleep(1)

        
            
    CloseHandle(process)
else:
    print("프로세서 열지 못함")