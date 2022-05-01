import socket
import asyncio

s = socket.socket()
s.settimeout(5)


async def check_host(host):
    with open('ips.txt', 'a') as file:
        try:
            s.connect((host, 22))
        except:
            print('no', host)
            return False
        else:
            print('yes', host)
            file.write(host + '\n')


async def main():
    for o in range(256 - 180):
        o += 180
        for k in range(256):
            #k += 197
            for i in range(256):
                #i += 108
                for j in range(256):
                    #j += 111
                    task = asyncio.create_task(check_host(str(o) + '.' + str(k) + '.' + str(i) + '.' + str(j)))
                    await task

if __name__ == '__main__':
    asyncio.run(main())
