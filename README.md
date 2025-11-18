
# Data Structures & Algorithms group project
This is the repository where Data Structure & Algorithm group project will be developed

### Setup virtual environment (Linux)
```sh
python -m venv .venv # Setup new virtual environment
source .venv/bin/activate
pip install -e . # Install all dependencies (only needed to run tests)
```

### Testing
```sh
pytest
```

### Coverage
```sh
pip install coverage   # Install coverage package
coverage run -m pytest # Fetch coverage
coverage report        # Print the coverage in stdout
```

#### Report
This is the coverage report, it shows how much our implementation code is covered by our tests.
- 100% means that each line and possible branch is tested (and thus covered) by our tests.
- 0% means that the file is not covered by our tests


```sh
Name                               Stmts   Miss  Cover
------------------------------------------------------
src/_array.py                         27      2    93%
src/balance_tree.py                  103      0   100%
src/binary_search_tree.py             66      0   100%
src/binary_tree.py                    34      0   100%
src/container.py                     108     23    79%
src/deque.py                          47      3    94%
src/hash_map.py                       41      0   100%
src/hash_table.py                     40      0   100%
src/linked_list.py                   151     10    93%
src/queue.py                          37      3    92%
src/stack.py                          37      3    92%
src/tree.py                           28      0   100%
```
