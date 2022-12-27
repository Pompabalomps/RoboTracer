import argparse

parser = argparse.ArgumentParser(description="RoboTracer")

parser.add_argument("filepath", metavar="F", type=str, nargs="+", help="The file path RoboTracer will run")

fp = parser.parse_args().filepath