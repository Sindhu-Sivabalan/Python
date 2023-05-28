import subprocess


txt='netsh wlan show profiles'
with subprocess.Popen(txt.split(), stdout=subprocess.PIPE) as proc:
    mydata=proc.stdout.read()
    mydata=bytes.decode(mydata)

    allines=mydata.split('\n')
    for x in allines:
        if x.strip()[:16]=='All User Profile':
            print(x.split(':')[1])
