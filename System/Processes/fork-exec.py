"starts programs until you type 'q'"

import os

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:                                             # copy process
        os.execlp('python', 'python', '/home/jinwentan/Desktop/Advanced Programming/week13/System/Processes/child.py', str(parm)) # overlay program
        assert False, 'error starting program'               # shouldn't return
    else:
        print('Child is', pid)
        if input() == 'q': break
