import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="RoboTracer")
parser.add_argument("filepath", metavar="F", type=str, nargs="+", help="The file path RoboTracer will run")
fp = parser.parse_args().filepath[0]

def get_syscalls():
    syscalls = sp.Popen(['strace', "./"+fp], stdout=sp.PIPE).stdout.read().decode("utf-8").split('\n')
    print(syscalls)

get_syscalls()
