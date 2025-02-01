from abc import ABC, abstractmethod


class _SATSolver(ABC):
    """SAT solver.

    Abstract base class for SAT solvers. This class provides a common interface
    for all SAT solvers.

    Parameters
    ----------
    clauses : list[tuple[str]]
        A list of clauses in conjunctive normal form (CNF).

    Attributes
    ----------
    formula : str
        The formula of the problem.
    """

    def __init__(self, clauses: list[tuple[str]]):
        self._variable_table = {}
        self._variables = []
        self._clauses = [self._parse_clause(clause) for clause in clauses]
        self._unit_clauses = []
        self._pure_literals = []

    @property
    def formula(self):
        return " ∧ ".join(
            [self._clause_to_string(clause) for clause in self._clauses]
        )

    def _parse_clause(self, clause: tuple[str]) -> tuple[int]:
        """Parse a clause.

        Variables are encoded as numbers 0 to n-1, where n is the number of
        variables. Positive literals with variables encoded with integer
        x are encoded as 2x, and negated literals are encoded as 2*x + 1. A
        parsed clause is a tuple of encoded literals.

        Parameters
        ----------
        clause : tuple[str]
            A clause.

        Returns
        -------
        tuple[int]
            A parsed clause.
        """
        parsed_clause = []
        for literal in clause:
            negated = 1 if literal.startswith("~") else 0
            variable = literal[negated:]
            if variable not in self._variable_table:
                self._variable_table[variable] = len(self._variables)
                self._variables.append(variable)
            encoded_literal = self._variable_table[variable] << 1 | negated
            parsed_clause.append(encoded_literal)
        return tuple(set(parsed_clause))

    def _literal_to_string(self, literal: int):
        """Convert a literal to a string.

        Parameters
        ----------
        literal : int
            A literal.
        """
        sign = "¬" if literal & 1 else ""
        return sign + self._variables[literal >> 1]

    def _clause_to_string(self, clause: tuple[int]):
        """Convert a clause to a string.

        Parameters
        ----------
        clause : tuple[int]
            A clause.
        """
        return (
            "(" + " ∨ ".join(self._literal_to_string(l) for l in clause) + ")"
        )

    def model_to_string(self, model) -> str:
        """Convert a model to a human-readible string.

        Parameters
        ----------
        model : list
            A list of variable assignments.

        Returns
        -------
        str
            A human-readible string representation of the model.

        Examples
        --------
        Recover a set of variable assignments from a given model.

        >>> from npycomp.solvers import DPLL
        >>> clauses = [("x1", "x2"), ("~x1", "~x2")]
        >>> solver = DPLL(clauses)
        >>> model = solver.solve()
        >>> model
        [1, 0]
        >>> solver.model_to_string(model)
        x1 = 1, x2 = 1
        """
        output = []
        for i, assignment in enumerate(model):
            if assignment is None:
                output.append(f"{self._variables[i]} ∈ {{0, 1}}")
            else:
                output.append(f"{self._variables[i]} = {assignment}")

        return ", ".join(output)

    @abstractmethod
    def solve(self) -> list[int]:
        """Solve a SAT problem.

        Returns
        -------
        list[int] | False
            A satisfying assignment if one exists, or False otherwise.

        Examples
        --------
        Solve a SAT problem defined by a list of clauses.

        >>> from npycomp.solvers import DPLL
        >>> clauses = [("x1", "~x2"), ("x1", "x2")]
        >>> solver = DPLL(clauses)
        >>> model = solver.solve()
        >>> model
        [1, None]
        >>> solver.model_to_string(model)
        x1 = 1, x2 ∈ {0, 1}

        Reduce a problem to SAT and solve it.

        >>> from npycomp.problems import Clique
        >>> A = [
        ...     [0, 1],
        ...     [1, 0],
        ... ]
        >>> k = 2
        >>> clique = Clique(A, k)
        >>> clauses = clique.reduce("SAT")
        >>> solver = DPLL(clauses)
        >>> model = solver.solve()
        [1, 0, 0, 1]
        """
        pass
