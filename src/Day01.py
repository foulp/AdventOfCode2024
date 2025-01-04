from pathlib import Path
import pandas as pd
import re

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        locations = f.read().split('\n')
    left, right = [], []
    for line in locations:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    left = sorted(left)
    right = sorted(right)
    print(f"The result of first star is {sum(abs(a-b) for a,b in zip(left, right))}")

    similarity = 0
    for a in left:
        similarity += right.count(a) * a
    print(f"The result of second star is {similarity}")