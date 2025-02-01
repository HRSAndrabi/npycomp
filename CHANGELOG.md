# CHANGELOG


## v0.2.0 (2025-02-01)

### Documentation

* docs: add reduction autosummaries. ([`b542107`](https://github.com/HRSAndrabi/npycomp/commit/b5421071c974b36f2ddffcb4bdb9ba66ed1221fc))

### Features

* feat: add 3sat to sat link. ([`a7359f0`](https://github.com/HRSAndrabi/npycomp/commit/a7359f0656c1115aa3548b70bcb0243fe60d01b0))


## v0.1.1 (2025-02-01)

### Bug Fixes

* fix: \`Problem\`should be initialised with args, not kwargs.

All reduction functions return args for the corresponding
reduced problem, not kwargs. \`Problem.__init__()\` expects kwargs,
resulting in errors. Refactored to excepts args instaed of kwargs. ([`ea5c22e`](https://github.com/HRSAndrabi/npycomp/commit/ea5c22e478b58cf3ad16a4da2329ff47907202b9))

### Documentation

* docs: add 3sat autosummary directive. ([`79db04a`](https://github.com/HRSAndrabi/npycomp/commit/79db04a1a15bcafdfd812f5fb245fa1891026dd6))


## v0.1.0 (2025-02-01)

### Build System

* build: install tox. ([`fde07e7`](https://github.com/HRSAndrabi/npycomp/commit/fde07e7f8b239f2b1f8901895c13f011c0dcbf44))

### Chores

* chore: ruff lint refactor. ([`ef91096`](https://github.com/HRSAndrabi/npycomp/commit/ef91096977bde480ac4de00c52fd0d501b4e6bea))

### Continuous Integration

* ci: test on py310-313. ([`9dd12c1`](https://github.com/HRSAndrabi/npycomp/commit/9dd12c1656df2eced4a22d7929fd584745d19b5d))

* ci: test workflow uses tox. ([`26d770e`](https://github.com/HRSAndrabi/npycomp/commit/26d770e2957c6c918c705b7eba47fd28d664fcfa))

### Documentation

* docs: add sphinx docs. ([`973476f`](https://github.com/HRSAndrabi/npycomp/commit/973476fe57c7ce8a8a1cbce74fb5e641ea222e30))

* docs: remove redundant docstring. ([`966e21a`](https://github.com/HRSAndrabi/npycomp/commit/966e21a41370ebf503b21538269b36d52bd57489))

### Features

* feat: add 3SAT and 3SAT to Clique reduction. ([`5f2abb9`](https://github.com/HRSAndrabi/npycomp/commit/5f2abb9b0d0a70e0260d4e7e92f0867993608f09))


## v0.0.1 (2025-01-28)

### Bug Fixes

* fix(Problem.reduce): inconsistant return type.

`Problem.reduce` should always return the args to the constructor
of the relevant reduction. However, `Problem.solve` expected a
dict of keyword args. This created an inconsistent bug where
`SAT.solve()` would work as expected, but other `Problem.solve()`s
would raise an error that a list of clauses were passed to the
constructor of `_SATSolver`, rather than a dict of keyword args.

Fixed by checking whether `Problem.solve()` is being invoked from
a SAT instance, so it can use the SAT keyword args directly. ([`7eabade`](https://github.com/HRSAndrabi/npycomp/commit/7eabade842a62d8fa78e3a13e6f6827e5ea9bc99))

* fix: raise error for not implemented reductions. ([`4c4c69b`](https://github.com/HRSAndrabi/npycomp/commit/4c4c69b237fe77751be8f0725064d88bd0ac5c3d))

* fix(reduce): handle not implemented problems. ([`905ae36`](https://github.com/HRSAndrabi/npycomp/commit/905ae36112fe68da55170206bbeafc41702d0640))

### Build System

* build: add matplotlib as doc requiremnet. ([`78fea98`](https://github.com/HRSAndrabi/npycomp/commit/78fea98b377fed4b1813b5968ace70fbbfe97c60))

### Documentation

* docs: add  class documentation. ([`a43f69c`](https://github.com/HRSAndrabi/npycomp/commit/a43f69cfc22cb56c2f000b8589af09c22586bc58))

* docs(SAT): provide formal exposition for . ([`e9d3856`](https://github.com/HRSAndrabi/npycomp/commit/e9d3856f7c06a05cd5a828fba7a9b316f367e4c7))

* docs: add autosummary of  and . ([`3ff11fb`](https://github.com/HRSAndrabi/npycomp/commit/3ff11fb637699a75bf4db7b40f198dc93578538e))

### Refactoring

* refactor: make  abstractmethod. ([`7e15643`](https://github.com/HRSAndrabi/npycomp/commit/7e15643127674476d3522ef3fbc563ce2a7e9e98))


## v0.0.0 (2025-01-27)

### Build System

* build: add lint, test, and release workflows. ([`5b8be61`](https://github.com/HRSAndrabi/npycomp/commit/5b8be61b6efa433e4d4e531fcabca4ac87922ab9))

### Chores

* chore: remove .DS_Store. ([`a9e7b30`](https://github.com/HRSAndrabi/npycomp/commit/a9e7b30e9a949ea356e015816ceab0c1d40bb787))

### Unknown

* Initial commit. ([`558e983`](https://github.com/HRSAndrabi/npycomp/commit/558e98365a91c998b495275b58720bb8cd2769b4))
