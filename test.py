import black
from functools import partial

fs = partial(black.format_str, line_length=88)


with open("./check.py","r") as thefile:
    source = thefile.read()

print("========================================================================")
print(fs(source))
