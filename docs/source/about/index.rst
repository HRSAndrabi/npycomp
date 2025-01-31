*******
About 
*******

.. rst-class:: lead

   Define, reduce, and solve NP-complete problems.

**NPyComp** (en·py·comp) is a Python package for NP-complete reductions. It provides a simple interface to define and reduce NP-complete problems.

I created this package as part of a research project. You can learn about me and my other projects by visiting my `personal website`_.


Features
------------

* Define NP-complete problems using a simple interface.
* Reduce NP-complete problems to other NP-complete problems.
* Solve NP-complete problems using a variety of SAT solvers.

Quick Start
-----------

Here's a quick example to get started with NPyComp:

.. code-block:: python

   from npycomp.problems import Clique, SAT

   clique = Clique(
      A = [
         [0, 1, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [0, 0, 0, 1]
      ],
      k = 3,
   )

   clauses = clique.reduce("SAT")
   sat = SAT(clauses)
   sat.solve()


Versioning 
----------
NPyComp follows the `Semantic Versioning standard`_. 

License
-------

NPyComp is open-source software, licensed under the MIT License. See the LICENSE file on `GitHub`_ for details.

.. _GitHub: https://github.com/HRSAndrabi/npycomp
.. _personal website: https://hassan.andra.bi
.. _Semantic Versioning standard: https://semver.org/