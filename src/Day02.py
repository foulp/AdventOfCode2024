from pathlib import Path
import pandas as pd
import re

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        reports = f.read().split('\n')
    n = 0
    n2 = 0
    for r in reports:
        report = list(map(int, r.split()))
        diff = [report[i+1] - report[i] for i in range(len(report)-1)]
        if all(0<d<=3 for d in diff) or all(-3<=d<0 for d in diff):
            n += 1
            n2 += 1
            continue
        for i in range(len(report)):
            d = report.pop(i)
            diff = [report[i+1] - report[i] for i in range(len(report)-1)]
            if all(0<d<=3 for d in diff) or all(-3<=d<0 for d in diff):
                n2 += 1
                break 
            report.insert(i, d)
    print(f"The result of first star is {n}")

    print(f"The result of second star is {n2}")