#process_file
import os
p='C:/GoDigital_Python_Codes/tuple.py'
if os.path.exists(p):
    process_file(p)
else:
    print(f'file does not exist{p}')
    
