from npycomp.solvers._solver import _SATSolver


class DPLL(_SATSolver):
    """Davis-Putnam-Logemann-Loveland (DPLL) solver for SAT.

    Implementation of The `Davis–Putnam–Logemann–Loveland`_ (DPLL) recursive
    backtracking procedure for solving the SAT problem. The algorithm runs by
    choosing a literal, assigning a truth value to it, simplifying the formula
    and then recursively checking if the simplified formula is satisfiable; if
    this is the case, the original formula is satisfiable; otherwise, the same
    recursive check is done assuming the opposite truth value.

    The DPLL algorithm improves over naive backtracking by applying
    `unit propagation`_ and pure literal elimination to simplify the formula at
    each step. These techniques reduce the total search space and improve the
    efficiency of the algorithm.

    **Unit propagation**. If a clause contains only one unassigned literal,
    the literal can be assigned to true, and all clauses containing the
    literal can be removed.

    **Pure literal elimination**. If a literal is pure if it appears with only
    one polarity in the formula. Pure literals can always be assigned in a way
    that makes the clauses containing them true.

    .. _Davis–Putnam–Logemann–Loveland: https://en.wikipedia.org/wiki/DPLL_algorithm
    .. _unit propagation: https://en.wikipedia.org/wiki/Unit_propagation

    Parameters
    ----------
    clauses : list[tuple[str]]
        A list of clauses in conjunctive normal form (CNF).
    """

    def __init__(self, clauses: list[tuple[str]]):
        super().__init__(clauses)

    def _unit_clauses_exist(self, clauses):
        """Check if unit clauses exist.

        A unit clause is a clause with only one unassigned literal.

        Parameters
        ----------
        clauses : list
            A list of clauses.
        """
        self._unit_clauses = [c for c in clauses if len(c) == 1]
        return bool(self._unit_clauses)

    def _unit_propagation(self, clauses, model):
        """Perform unit propagation.

        Remove every clause containing a unit clause's literaly, and remove
        the negation of the unit clause's literal from every clause.

        Parameters
        ----------
        clauses : list
            A list of clauses.
        model : list
            A list of variable assignments.
        """
        unit_literals = set([literal for (literal,) in self._unit_clauses])
        while unit_literals:
            literal = unit_literals.pop()
            clauses = [c for c in clauses if literal not in c]
            clauses = [
                tuple([l for l in c if l != literal ^ 1]) for c in clauses
            ]
            if model[literal >> 1] is None:
                model[literal >> 1] = int(literal & 1 == 0)

        return clauses, model

    def _pure_literals_exist(self, clauses):
        """Check if pure literals exist.

        A pure literal is a literal that appears with the same sign in all
        clauses.

        Parameters
        ----------
        clauses : list
            A list of clauses.
        """
        literals = set()
        for clause in clauses:
            literals.update(clause)
        pure_literals = set()
        for literal in literals:
            if literal ^ 1 not in literals:
                pure_literals.add(literal)

        self._pure_literals = pure_literals
        return bool(pure_literals)

    def _pure_literal_elimination(self, clauses, model):
        """Perform pure literal elimination.

        Remove every clause containing a pure literal, and assign the pure
        literal to the value that makes the clause true.

        Parameters
        ----------
        clauses : list
            A list of clauses.
        model : list
            A list of variable assignments.
        """
        for literal in self._pure_literals:
            clauses = [clause for clause in clauses if literal not in clause]
            model[literal >> 1] = int(literal & 1 == 0)
        return clauses, model

    def _dpll(self, clauses, model):
        """Perform the DPLL procedure.

        Parameters
        ----------
        clauses : list
            A list of clauses.
        model : list
            A list of variable assignments
        """
        # Unit propagation
        while self._unit_clauses_exist(clauses):
            clauses, model = self._unit_propagation(clauses, model)
        # Pure literal elimination
        while self._pure_literals_exist(clauses):
            clauses, model = self._pure_literal_elimination(clauses, model)
        # Stopping conditions
        if not clauses:
            return model
        if any(not clause for clause in clauses):
            return False

        # DPLL procedure
        try:
            variable = model.index(None)
        except:
            return False
        for literal in (variable << 1, variable << 1 | 1):
            solution = self._dpll(
                [*clauses, (literal,)],
                [
                    *model[:literal],
                    int(literal & 1 == 0),
                    *model[literal + 1 :],
                ],
            )
            if solution:
                return solution

        return False

    def solve(self):
        model = self._dpll(self._clauses, [None] * len(self._variables))
        return model
