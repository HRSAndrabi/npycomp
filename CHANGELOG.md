# CHANGELOG


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
