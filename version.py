Import("env")
import subprocess
import sys
print("Running version.py script...")

version = int(''.join(file('src/build')).replace('\n',''))
if subprocess.check_output(['git', 'status', '-s']):
    version = version + 1
env.Append(CPPDEFINES=("VERSION", version))
