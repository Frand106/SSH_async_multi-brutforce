import socket

s = socket.socket()
s.settimeout(3)

async def main():
    with open('ips.txt', 'a') as file:
        for i in range(256):
            for j in range(256):
                file.write('192.168.' + str(i) + '.' + str(j) + '\n')
