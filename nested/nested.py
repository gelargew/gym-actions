from os import walk
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR, 'countries.json')

with open(path, 'r') as f:
    print(f)