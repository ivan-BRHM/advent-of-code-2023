from pathlib import Path
from re import sub

data = Path("input_files/day_01.txt").read_text().split("\n")

result = []
for cal_val in data:
    digits = sub(r"[a-z]", "", cal_val)

    result.append(int(digits[0] + digits[-1]))

print(sum(result))
