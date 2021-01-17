
# coding: utf-8




import os
ipaddr = input('Enter the IP address:') 
stream = os.popen('ping -c 4 {}'.format(ipaddr)) 
output = stream.read() 
if '0 received' in output: 
    print('IP unreachable') 
else: 
    print('IP reachable') 
    print(output)





import subprocess
def run_command(command):
    p = subprocess.Popen(command,
    stdout = subprocess.PIPE,
    stderr = subprocess.STDOUT)
    return iter(p.stdout.readline, b'')
if list(run_command("java -version")):
    print(True)
if list(run_command("aws -version")):
    print('Software is installed')
else:
    print('Software not installed')

