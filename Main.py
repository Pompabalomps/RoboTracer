import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="RoboTracer")
parser.add_argument("filepath", metavar="F", type=str, nargs="+", help="The file path RoboTracer will run")
fp = parser.parse_args().filepath[0]

process = sp.Popen(['strace', "./"+fp], stdout=sp.PIPE, stderr=sp.PIPE)

def get_syscalls(proc):
    syscalls = proc.stdout.read().encode("utf-8").split("\n")
    return syscalls

print(get_syscalls(process))
