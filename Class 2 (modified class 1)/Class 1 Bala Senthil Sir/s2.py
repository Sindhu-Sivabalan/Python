import subprocess


txt='netsh wlan show profiles "Home_5G" key=clear '
with subprocess.Popen(txt.split(), stdout=subprocess.PIPE) as proc:
    mydata=proc.stdout.read()
    mydata=bytes.decode(mydata)
    for i in mydata.split('\n'):
        if i.strip()[:11]=='Key Content':
            print(i.split(':')[1])
