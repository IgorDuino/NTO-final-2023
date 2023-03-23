import os

for filename in os.listdir():
    if filename.split('.')[-1] not in ('py', 'exe'):
        res = os.popen(f"mono geeks.exe {filename}").read()
        a = '.'.join(filename.split('.')[:-1])
        with open(f'res/dec_{a}', 'wb') as f:
            f.write(bytes.fromhex(res.replace('-', '')))
