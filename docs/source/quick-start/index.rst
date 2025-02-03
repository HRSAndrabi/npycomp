Quick start
=====

.. rst-class:: lead
	
	Get started by defining a problem instance.




Installation
-----------

First, install NPyComp using pip, or by following the alternative installation methods in the `Installation guide`_.

.. code-block:: bash

	pip install npycomp

Basic Usage
----------

Let's walk through a simple example of using NPyComp to define and solve a 3-SAT problem.

.. code-block:: python

    from npycomp.problems import SAT

    # Define a 3-SAT problem
    sat = SAT(clauses=[
        ["a", "b", "c"],
        ["~a", "~b", "c"],
        ["a", "~b", "~c"],
    ])

    # Solve the problem
    solution = sat.solve()

We can also reduce the 3-SAT problem to a Clique problem:

.. code-block:: python

    from npycomp.problems import Clique

    # Reduce the SAT problem to a Clique problem
    clique = sat.reduce(Clique)

    # Solve the resulting Clique problem
    solution = clique.solve()

The full list of problems supported by NPyComp can be found in the `Problems`_ section of the `API Reference`_.
Each problem can be reduced to any other problem in the library using the ``reduce()`` method.

Using DIMACS files
------------------

NPyComp supports loading problem instances from DIMACS format files. 
For more information on the DIMACS format, see the `MaxSat 2023 Evaluation Rules`_.

.. code-block:: python

    # Load a SAT instance
    sat = SAT.from_dimacs("path/to/problem.cnf")

    # Load a Clique instance (requires specifying k)
    clique = Clique.from_dimacs("path/to/graph.clq", k=5)



.. _Installation guide: /installation/index.html
.. _Problems: /reference/generated/npycomp.problems.html
.. _API Reference: /refernece/index.html
.. _Contributing: /contributing/index.html
.. _GitHub repository: https://github.com/HRSAndrabi/npycomp
.. _MaxSat 2023 Evaluation Rules: https://maxsat-evaluations.github.io/2023/rules.html




