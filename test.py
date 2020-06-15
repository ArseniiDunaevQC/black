import black
from functools import partial

fs = partial(black.format_str, mode=black.Mode(
    target_versions={black.TargetVersion.PY36},
    line_length=88,
    string_normalization=False,
    is_pyi=False,
))


with open("./check.py", "r") as thefile:
    source = thefile.read()

print("========================================================================")
print(fs(source))
