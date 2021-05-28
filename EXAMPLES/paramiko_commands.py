#!/usr/bin/env python
import sys
import paramiko

ssh = None

with paramiko.SSHClient() as ssh:  # <1>

    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # <2>

        ssh.connect('localhost', username='python', password='l0lz')  # <3>

        stdin, stdout, stderr = ssh.exec_command('whoami')  # <4>
        print(stdout.read().decode())  # <5>
        print('-' * 60)

        stdin, stdout, stderr = ssh.exec_command('ls -l')  # <4>
        print(stdout.read().decode())  # <5>
        print('-' * 60)

        stdin, stdout, stderr = ssh.exec_command('ls -l /etc/passwd /etc/horcrux')  # <4>
        print("STDOUT:")
        print(stdout.read().decode())  # <5>
        print("STDERR:")
        print(stderr.read().decode())  # <6>
        print('-' * 60)
    except Exception as err:
        print(err)
    finally:
        if ssh is not None:
            ssh.close()

        del stdin, stdout, stderr, ssh  # DO THIS (ugh)


