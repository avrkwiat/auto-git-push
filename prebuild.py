Import("env")
import subprocess
import sys
print("Running prebuild.py script...")

env.Execute("git fetch")
if subprocess.check_output(['git', 'diff', 'HEAD', 'origin/master']):
    print("ZROB PULLA KURWA!!!")
    sys.exit(1)

version = int(''.join(file('src/build')).replace('\n',''))

print("Looking for source changes")
if subprocess.check_output(['git', 'status', '-s']):
    print("Source changed. Incrementing build number...")
    version = version + 1
    env.Append(CPPDEFINES=("VERSION", version))
else:
    print("No changes")

env.Replace(PROGNAME="test-%s" % version)
