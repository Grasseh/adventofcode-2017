# pylint: disable=missing-docstring
def solve(fn_input):
    return sum(map(int, filter(str.isdigit, fn_input)))
