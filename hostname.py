import socket

hostname = socket.gethostname()
print(f'My hostname is: {hostname}')
ipaddress = socket.gethostbyname(hostname)
print(f'My IP address is: {ipaddress}')
dns = socket.gethostbyaddr(hostname)
dns2 = socket.gethostbyaddr(ipaddress)
print(dns, dns2)