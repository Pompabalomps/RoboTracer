import argparse
import subprocess as sp

parser = argparse.ArgumentParser(description="RoboTracer")
parser.add_argument("filepath", metavar="F", type=str, nargs="+", help="The file path RoboTracer will run")
fp = parser.parse_args().filepath[0]

process = sp.check_output(['strace', "./"+fp], stderr=sp.STDOUT, timeout=10) # running strace on the process with timeout of 10 seconds

def get_syscalls(proc):
    syscalls = proc.decode("utf-8").split("\n") # get all syscalls from strace
    return syscalls[:len(syscalls)-1] # remove final exit message

def print_header_syscalls(syscalls):
    for i in range(min(16, len(syscalls))): # iterating over 16 first syscalls(or less if not enough)
        print(syscalls[i])