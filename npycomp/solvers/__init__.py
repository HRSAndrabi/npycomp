"""Implementations of SAT solvers.

NPyComp ``solvers`` provides implementations of solvers for the SAT problem.
Each solver in this module is a class that implements a method for solving
an instance of the SAT problem.

Solvers
-------
.. autosummary::
   :toctree: solvers

   DPLL - Davis-Putnam-Logemann-Loveland (DPLL) solver for SAT.
"""

from npycomp.solvers._dpll import DPLL
