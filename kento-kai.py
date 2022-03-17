#!/usr/bin/env python3
import sys
import datetime


def print_usage():
    print("Usage: ", end="")
    print(args[0] + " ", end="")
    print("10 ", end="")  # ARG1: number of column (ex. 10)
    print("7 ", end="")  # ARG2: number of column (ex. 10)
    print("1 ", end="")  # ARG3: number of column (ex. 10)
    print("1 ", end="")  # ARG4: number of column (ex. 10)
    print("20200324 ", end="")  # ARG5: start date (ex. 20200324)
    print("20200630 ", end="")  # ARG6: end date (ex. 20200324) or nothing
    print()
    print("ARG1: Number of column")
    print("ARG2: Difference between continuous 2days")
    print("ARG3: Print Week Days (Yes=>1, No=>other)")
    print("ARG4: Color Mode  (Yes=>1, No=>other)")
    print("ARG5: Start date")
    print("ARG6: End date (Nothig is ok)")


args = sys.argv

MAX = 30
mode = 0
weeks = ["月", "火", "水", "木", "金", "土", "日"]
weeks_prefix = ['', '', '', '', '',
                '<rowbgcolor="#bce2e8">', '<rowbgcolor="#f6bfbc">']
# print_week = False
# print_week = True
# DIFF = 1
# DIFF = 7

mode = len(args) - 1


if mode == 4:
    d1 = datetime.date.today()
elif mode == 5:
    start_date = args[5]
    d1 = datetime.datetime.strptime(start_date, "%Y%m%d")
elif mode == 6:
    start_date = args[5]
    end_date = args[6]
    d1 = datetime.datetime.strptime(start_date, "%Y%m%d")
    d2 = datetime.datetime.strptime(end_date, "%Y%m%d")
else:
    print("Error!!!")
    print_usage()
    exit(1)

columns = int(args[1])
diff = int(args[2])
print_week = True if int(args[3]) == 1 else False
color_mode = True if int(args[4]) == 1 else False

counter = 0
if print_week:
    printed_format = "{0:%-m/%-d}({1})"
    # -m, -dとすることで0埋めしない
else:
    printed_format = "{0:%-m/%-d}"


while True:
    printed_str = printed_format.format(d1, weeks[d1.weekday()])
    if color_mode == True:
        printed_str = weeks_prefix[d1.weekday()] + printed_str
    printed_str = "||" + printed_str + " ||"

    print(printed_str + "".join([" ||"]*columns))

    d1 += datetime.timedelta(days=diff)
    if mode == 6 and d1 > d2:
        break
    elif mode is not 6 and counter >= MAX:
        break
    counter += 1
