from pathlib import Path
import pandas as pd
import re

if __name__ == '__main__':
    with open(f'../inputs/{Path(__file__).stem}.txt', 'r') as f:
        memory = f.read()

    s = 0
    p = re.compile(r'mul\((\d+),(\d+)\)')
    for m in p.findall(memory):
        s += int(m[0]) * int(m[1])
        
    print(f"The result of first star is {s}")
    
    s = 0
    p2 = re.compile(r'do\(\)')
    p3 = re.compile(r'don\'t\(\)')
    enabled = 1
    while memory:
        m1 = p.search(memory)
        if enabled == 1:
            m2 = p3.search(memory)
        else:
            m2 = p2.search(memory)
        if m1 is None:
            break 
        if m2 is None or m1.start() < m2.start():
            if enabled == 1:
                s += int(m1.group(1)) * int(m1.group(2))
            memory = memory[m1.end():]
        else:
            enabled = enabled * -1 + 1
            memory = memory[m2.end():]
    print(f"The result of second star is {s}")