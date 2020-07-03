"""
Auto open specified item on close
License - MIT
Author - Jack Bayliss 03/07/2020
"""
import subprocess,platform,time,configparser
from subprocess import CREATE_NEW_CONSOLE

class RestartMe:
 def __init__(self):
    config = configparser.ConfigParser()
    config.read('config.ini')
    self.Handler(config['DEFAULT']['target'])
    
 def Handler(self,file):
    # Open file subprocess in a new window.
    p = subprocess.Popen(file,creationflags=CREATE_NEW_CONSOLE)
    poll = p.poll()
    # While the poll is None, it's fine- no don't restart.
    while p.poll() is None:
        # Sleep to ensure we're not throttling the CPU.
        time.sleep(1)
    else:
        # Restart the process
        RestartMe()

RestartMe()
