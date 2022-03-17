#!/usr/bin/env python3
import sys
import datetime
import subprocess


def print_usage():
    print("Usage: ", end="")
    print(args[0] + " ", end="")
    print("20200324 ", end="")  # ARG1: start date (ex. 20200324)
    print()
    print("ARG1: Start date (Nothig is ok)")


args = sys.argv

MAX = 10 #出力行数
mode = 0
DIFF = 7 #日にち間隔

mode = len(args)

if mode == 1:
    d1 = datetime.date.today()
elif mode == 2:
    start_date = args[1]
    d1 = datetime.datetime.strptime(start_date, "%Y%m%d")
else:
    print("Error!!!")
    print_usage()
    exit(1)

counter = 0

while True:
    str_for_input = "{0:%Y%m%d}".format(d1)
    subprocess.run(["./mkmtggrid.pl", str_for_input])
    d1 += datetime.timedelta(days=DIFF)
    if counter >= MAX:
        break
    counter += 1
