class ReluplexConfiguration:

    def __init__(self, basis=None, tableau=None, lb=None, ub=None, alpha=None, relu_connections=None):
        self.basis = set() if basis is None else basis
        self.tableau = set() if tableau is None else tableau
        self.lb = dict() if lb is None else lb
        self.ub = dict() if ub is None else ub
        self.alpha = dict() if alpha is None else alpha
        self.relu_connections = list() if relu_connections is None else relu_connections

