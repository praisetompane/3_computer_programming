import sys
from pprint import pprint       

1. check that your module path is in Python's search tree: pprint(sys.path)
    first entry is either: 
        path to the script executed
        '' := instructs python to search current directory
2. check modules accessible to Python: pprint(sys.modules)
3. run python with default sys.path: python3 -S
    sometimes sys.path changed by package managers
2. clear out __pycache__                                                                                