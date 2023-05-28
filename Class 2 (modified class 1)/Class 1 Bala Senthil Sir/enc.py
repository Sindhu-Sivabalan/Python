import nmap

nm=nmap.PortScanner()
x=nm.scan(hosts='192.168.246.0/24')
print(x)