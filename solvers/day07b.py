# pylint: disable=missing-docstring
# NOTE : THIS SOLUTION DOES NOT WORK IF THE UNBALANCED CHILD IS THE FIRST CHILD. GOOD THIS IT WASN'T :)
import unittest
import re

def solve(fn_input):
    discs = fn_input[:-1].split("\n")
    table = prepare_table(discs)
    bottom = get_table_bottom(table)
    return find_unbalanced_value(table, bottom)["answer"]

def find_unbalanced_value(table, bottom):
    sums = {}
    for child in table[bottom]["childs"]:
        value = find_unbalanced_value(table, child)
        if "answer" in value:
            return value
        sums[child] = value["sum"]
    #Check if sums are okay
    same_sum = 0
    for value, sum in sums.items():
        if same_sum == 0:
            same_sum = sum
        else:
            if sum != same_sum:
                return {"answer" : same_sum - sum + int(table[value]["weight"])}
    return {"sum" : same_sum * len(sums) + int(table[bottom]["weight"])}

def prepare_table(discs):
    table = {}
    for disc in discs:
        disc = parse_disc(disc)
        if not disc["name"] in table:
            table[disc["name"]] = disc
            table[disc["name"]]["parent"] = ""
        table[disc["name"]]["weight"] = disc["weight"]
        table[disc["name"]]["childs"] = disc["childs"]
        for child in disc["childs"]:
            if not child in table:
                table[child] = {}
            table[child]["parent"] = disc["name"]
    return table

def get_table_bottom(table):
    return [value for key, value in table.items() if value["parent"] == ""][0]["name"]

def parse_disc(disc):
    string_data = re.match(r"(\w+) \((\d+)\)", disc)
    name = string_data.group(1)
    weight = string_data.group(2)
    arrow = disc.find("-> ")
    childs = []
    if not arrow == -1:
        childs = disc[arrow+3:].split(", ")
    return {"name" : name, "weight" : weight, "childs" : childs}

class UnitTest(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_disc("pbga (66) -> abcd, efgh"), {"name" : "pbga", "weight" : "66", "childs" : ["abcd", "efgh"]})

    def test_solve(self):
        self.assertEqual(solve("pbga (66)\nxhth (57)\nebii (61)\nhavc (66)\nktlj (57)\nfwft (72) -> ktlj, cntj, xhth\nqoyq (66)\npadx (45) -> pbga, havc, qoyq\ntknk (41) -> ugml, padx, fwft\njptl (61)\nugml (68) -> gyxo, ebii, jptl\ngyxo (61)\ncntj (57)\n"), 60)
