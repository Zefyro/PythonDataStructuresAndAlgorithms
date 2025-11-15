
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
