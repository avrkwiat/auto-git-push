Import("env")
import subprocess
import sys
print("Running postbuild.py script...")

def postbuild(source, target, env):
    if subprocess.check_output(['git', 'status', '-s']):
        with open(r'src/build','r+') as f:
            value = int(f.read())
            f.seek(0)
            f.write(str(value + 1))
        env.Execute("git add .")
        build = ''.join(file('src/build')).replace('\n','')

        env.Execute("git commit -m \"auto commit build %s\"" % build)
        env.Execute("git tag -a %s -m \"automated tagging\""  % build)
        env.Execute("git push origin %s"  % build)
        env.Execute("git push origin master")
    else:
        print("No changes")

env.AddPreAction("upload", postbuild)
