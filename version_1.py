import wmi

ti = 0 

names = [
    'amdfendrsr.exe',
    'atieclxx.exe',
    'atiesrxx.exe',
    'AUEPMaster.exe',
    'AUEPDU.exe',
]

f = wmi.WMI()

for process in f.Win32_Process():
    for name in names:
        if process.name == name:
            process.Terminate()
            ti += 1

if ti == 0:
    print("Process not found.")