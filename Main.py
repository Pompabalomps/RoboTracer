import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="RoboTracer")
parser.add_argument("filepath", metavar="F", type=str, nargs="+", help="The file path RoboTracer will run")
fp = parser.parse_args().filepath[0]

process = sp.check_output(['strace', "./"+fp], stderr=sp.STDOUT)

def get_syscalls(proc):
    syscalls = proc.stderr.read().decode("utf-8").split("\n")
    return syscalls

print(get_syscalls(process))
