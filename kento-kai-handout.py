#!/usr/bin/env python3
from itertools import count
from locale import MON_1
from operator import le
import sys
import datetime
import re

# ("名前", 何周目)
lab_menber_list_M2 = [("r-kato", 1),("takeya", 2), ("okuda", 1), ("nakahara", 3), ("k-yamamoto", 2)]
lab_menber_list_M1 = [("s-shiraki", 1), ("nomura", 2), ("t-yamamoto", 3),("y-watanabe", 3), ("nihommatsu", 1), ("miwagawa", 2)]
lab_menber_list_B4 = [("aoba", 1), ("s-sato", 2), ("m-tsuduki", 2), ("y-hoshi", 3), ("a-yamada", 3), ("zhang", 3), ("n-kamiya", 1), ("s_sakai", 1), ("tatsumi", 2), ("fujie", 3)]

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

# suffix = weeks[d1.weekday] 
# suffix kentoukai = -ken-[date]

suffix_ken = "-ken-" 
suffix_filename_extention = ".pptx"

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


if mode == 3:
    d1 = datetime.date.today() 
elif mode == 4:
    start_date = args[4]
    d1 = datetime.datetime.strptime(start_date, "%Y%m%d")
elif mode == 5:
    start_date = args[4]
    end_date = args[5]
    d1 = datetime.datetime.strptime(start_date, "%Y%m%d")
    d2 = datetime.datetime.strptime(end_date, "%Y%m%d")
else:
    print("Error!!!")
    print_usage()
    exit(1)

columns = len(lab_menber_list_B4) + len(lab_menber_list_M1) + len(lab_menber_list_M2)
_, duty_list_M2 = zip(*lab_menber_list_M2)
_, duty_list_M1 = zip(*lab_menber_list_M1)
_, duty_list_B4 = zip(*lab_menber_list_B4)
duty_span_M2 = max(duty_list_M2)
duty_span_M1 = max(duty_list_M1)
duty_span_B4 = max(duty_list_B4)

diff = int(args[1])
print_week = True if int(args[2]) == 1 else False
color_mode = True if int(args[3]) == 1 else False

duty_M2, duty_M1, duty_B4 = 0, 0, 0

counter = 0
if print_week:
    printed_format = "{0:%-m/%-d}({1})"
    # -m, -dとすることで0埋めしない
else:
    printed_format = "{0:%-m/%-d}"

while True:
    suffix_ken = "-ken-" 
    suffix_filename_extention = ".pptx|資料]]"
    printed_str = printed_format.format(d1, weeks[d1.weekday()])
    datetext = str(d1)
    suffix_date = re.sub("|-", "", datetext[:datetext.find(' ')])
    suffix_text = suffix_ken + suffix_date + suffix_filename_extention
    if color_mode == True:
        printed_str = weeks_prefix[d1.weekday()] + printed_str
    printed_str = "||" + printed_str + " ||"        
    
    print(printed_str, end='')
    for index in range(len(lab_menber_list_M2)):
        if lab_menber_list_M2[index][1] == duty_M2 + 1:
            print("[[attachment:" + lab_menber_list_M2[index][0] + suffix_text + "".join([" ||"]), end='')
        else:
            print(" ||", end='')
    for index in range(len(lab_menber_list_M1)):
        if lab_menber_list_M1[index][1] == duty_M1 + 1:
            print("[[attachment:" + lab_menber_list_M1[index][0] + suffix_text + "".join([" ||"]), end='')
        else:
            print(" ||", end='')
    for index in range(len(lab_menber_list_B4)):
        if lab_menber_list_B4[index][1] == duty_B4 + 1:
            print("[[attachment:" + lab_menber_list_B4[index][0] + suffix_text + "".join([" ||"]), end='')
        else:
            print(" ||", end='')
    print() # 改行

    duty_M2 = (duty_M2 + 1) % duty_span_M2
    duty_M1 = (duty_M1 + 1) % duty_span_M1
    duty_B4 = (duty_B4 + 1) % duty_span_B4

    d1 += datetime.timedelta(days=diff)
    if mode == 5 and d1 > d2:
        break
    elif mode is not 5 and counter >= MAX:
        break

    counter += 1