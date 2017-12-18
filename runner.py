# pylint: disable=missing-docstring
import importlib
import sys
import time
import os

def main():
    print("Welcome to Grasseh's 2017 Advent of Code")
    print("Currently running performance tests")
    files = os.listdir("solvers")
    files = filter(lambda y: os.path.isfile(os.path.join("solvers", y)), files)

    problems = list(map(lambda y: y[3:6], files))
    problems = list(filter(lambda y: y[:-1] != "00", problems))
    problem_list = []
    for problem_no in problems:
        try:
            text_file = open("inputs/day{}.txt".format(problem_no[:-1]))
            content = text_file.read()
            solver = importlib.import_module("solvers.day{}".format(problem_no))
        except IOError:
            print("Problem file not found(input or solver)")
            print(problem_no)
            sys.exit(0)
        no_runs = 100
        sum_runs = 0
        for _run in range(0, no_runs):
            now = time.time()
            _solution = solver.solve(content)
            this_run_time = (time.time() - now) * 1000
            sum_runs += this_run_time
        execution_time = sum_runs / no_runs
        problem_list.append({"number" : problem_no, "time" : execution_time})

        print("Problem {} solved in {:10.4f} ms (average for {} runs)".format(\
              problem_no, execution_time, no_runs))
    write_results(problem_list)

def write_results(problems):
    file = open("performance.md", "w")

    file.write("| Day | Problem a (ms) | Problem b (ms) |\n")
    file.write("|-----|---------------:|---------------:|\n")
    problems = sorted(problems, key=lambda x: x["number"])
    for i in range(0, len(problems) // 2):
        file.write("|{0}   |{1:10.4f}      |{2:10.4f}      |\n".format(\
             problems[i * 2]["number"][:-1], \
             problems[i * 2]["time"], \
             problems[i * 2 + 1]["time"]))
    file.close()

main()
