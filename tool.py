import win32process
import win32api
import psutil

def Getpid(process_name : str):
    for proc in psutil.process_iter():
        if process_name in proc.name():
            return proc.pid

def get_base_addr(process_name : str) -> hex:
    process_pid = Getpid(process_name)
    if process_pid == None:
        return None

    # first get pid, see the 32-bit solution

    PROCESS_ALL_ACCESS = 0x1F0FFF
    processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, process_pid)
    modules = win32process.EnumProcessModules(processHandle)
    processHandle.close()
    base_addr = modules[0]
    return base_addr