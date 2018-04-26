import sys
import subprocess

ret = subprocess.call(['pytest', '.'])
if ret != 0:
    sys.stderr.write(str(ret))