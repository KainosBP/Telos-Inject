# process.py
# ----------
# By: J.T. Buice - KainosBP
# 
#  Using the Telos Snapshot from: https://github.com/Telos-Foundation/snapshots/raw/master/tlos_genesis_snapshot.csv
#
#  stdin w/ pipe:
#   cat example.csv | python3 process.py
#
# filename as arg:
#   python3 process.py example.csv
#
# The output of this script is sent to stdout, which allows you to pipe it to a file or another processing target
# Like: cat tlos_genesis_snapshot.csv | python3 process.py &>> processsnap.csv
# The script takes about 5 seconds to run.
#
#          if token_amt <=3 then .1
#          if token_amt >3 and <=11 then 2
#          if token_amt > 11 then 10
#
#         token_amt - liquid = remainder
#         Remainder / 2 = CPU
#         Remainder - CPU = BW
#
#   The resultant CSV columns are:
#   Genesis,EOS_key,liquid,CPU,BW,token_amt

import csv
import sys

def process_row(row):
    genesis = row[2]
    eos_key = row[3]
    token_amt = float(row[4])
    liquid = 0.1

    if token_amt > 3 and token_amt <= 11:
        liquid = 2
    if token_amt > 11:
        liquid = 10

    remainder = token_amt - liquid
    cpu = float('{0:.4f}'.format(remainder / 2))
    bw = remainder - cpu

    cpu = cpu
    bw = bw

    cpu_str = str(cpu)
    bw_str = str(bw)

    new_row = {
        'Genesis': genesis,
        'EOS_key': eos_key,
        'liquid': liquid,
        'CPU': round(cpu, 4),
        'BW': round(bw, 4),
        'token_amt': token_amt
    }

    return new_row

def process_file(file_contents):
    output = []
    line_count = 0
    for row in csv.reader(file_contents):
        if line_count > 0:
            output.append(process_row(row))
        line_count += 1
    return output

def write_csv(output):
    fieldnames = ['Genesis', 'EOS_key', 'liquid', 'CPU', 'BW', 'token_amt']
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

    writer.writeheader()
    for row in output:
        writer.writerow(row)

def run():
    if len(sys.argv) >= 2:
        # open file passed in as the first arg
        file_contents = open(sys.argv[1])
    else: 
        # open stdin for piped file content
        file_contents = iter(sys.stdin.readline, '')

    output = process_file(file_contents)
    write_csv(output)

run()
