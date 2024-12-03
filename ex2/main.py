from pathlib import Path
from itertools import pairwise

safe_reports_count = 0
double_checked_reports = 0

def is_safe(my_list):
    my_list_copy = my_list.copy()
    increasing_order = None
    
    for n1, n2 in pairwise(my_list_copy):
        if increasing_order is None:
            increasing_order = (n1 < n2)
        if (increasing_order and n1>n2) or (not increasing_order and n2>n1):
            return False
        if not 0 < abs(n1-n2) <= 3:
            return False

    return True


for line in Path('input.txt').read_text().splitlines():
    reports = list(map(int,line.split(' ')))
    
    if is_safe(reports):
        safe_reports_count += 1
        continue

    partial_report_ok = False
    for i in range(len(reports)):
        if partial_report_ok:
            break
        partial_report_ok = is_safe([b for a,b in enumerate(reports) if a!=i])
    if partial_report_ok:
        double_checked_reports += 1

print(safe_reports_count)
print(safe_reports_count+double_checked_reports)