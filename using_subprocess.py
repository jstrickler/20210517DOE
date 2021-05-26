from subprocess import run, Popen, PIPE, CalledProcessError
import shlex
from glob import glob

cmd = "netstat -an"
cmd_words = shlex.split(cmd)

file_args = glob('DATA/p*.txt')

cmd_words += file_args

print(cmd_words)

try:
    proc = run(cmd_words, stdout=PIPE)
    # run(cmd, shell=True)
except CalledProcessError as err:
    print(err)
    print(err.returncode)
else:
    # proc.returncode
    output = proc.stdout.decode()  # decode captured UTF-8 string
    all_lines = output.splitlines()
    for line in all_lines:
        if "ESTAB" in line:
            proto, recv, send, local, remote, _ = line.split()
            print(f"{local:30s} {remote:30s}")

print('-' * 60)


pipe_cmd = "ps -aef | grep doc | grep 501 | awk '{ print $1, $2 }'"

run(pipe_cmd, shell=True)










