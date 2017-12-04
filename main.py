# pylint: disable=missing-docstring
import importlib
import sys
import time

def main():
    print("Welcome to Grasseh's 2017 Advent of Code")
    print("Enter your problem number")
    problem_no = input(">")
    try:
        text_file = open("inputs/day{}.txt".format(problem_no[:-1]))
        content = text_file.read()
        solver = importlib.import_module("solvers.day{}".format(problem_no))
    except IOError:
        print("Problem file not found(input or solver)")
        sys.exit(0)
    now = time.time()
    solution = solver.solve(content)
    execution_time = (time.time() - now) * 1000
    print("The solution to problem {} is : {}".format(problem_no, solution))
    print("Execution complete in {:10.4f} ms".format(execution_time))

main()
