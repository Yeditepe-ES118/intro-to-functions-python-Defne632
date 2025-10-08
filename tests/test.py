import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)  # Adjust based on your structure
print(parent_dir)
sys.path.insert(0, parent_dir)

from lab2 import find_circumference

@pytest.fixture
def get_results():
    num_arr = np.loadtxt("tests/num_arr.csv", delimiter=",")
    return num_arr

def test_values_arr(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_a = np.int64(np.loadtxt("tests/test_a"+str(i)+".csv", delimiter=","))
        test_b = np.int64(np.loadtxt("tests/test_b"+str(i)+".csv", delimiter=","))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        res = find_circumference(test_a, test_b)

        assert res.all() == true_res.all()
