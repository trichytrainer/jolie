import sys
import subprocess

ret = subprocess.call(['pytest', '.'])
if ret == 0:
    sys.stdout.write('0')
else:
    sys.stderr.write('1')