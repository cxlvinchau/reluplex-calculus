from typing import List, Dict

VARIABLE_ID = 0


class Variable:

    def __init__(self, name: str):
        global VARIABLE_ID
        self.name = name
        self.id = VARIABLE_ID
        VARIABLE_ID += 1

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, Variable):
            return other.id == self.id
        return False


class Equation:

    def __init__(self, basic_var: Variable, rhs: Dict):
        self.basic_var = basic_var
        self.rhs = rhs

    def __hash__(self):
        return hash(self.basic_var)

    def __eq__(self, other):
        if isinstance(other, Equation):
            return other.basic_var.id == self.basic_var.id
        return False
