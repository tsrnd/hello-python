import cocktailShakerSort
import pytest

testdata = [
    ([1,3,4,4,7,23,53,75,34,2,54,3,3,6,245], [1, 2, 3, 3, 3, 4, 4, 6, 7, 23, 34, 53, 54, 75, 245]),
    ([5,3,4,6,3,6,8,43,653,436,666,777,33,224,65], [3, 3, 4, 5, 6, 6, 8, 33, 43, 65, 224, 436, 653, 666, 777]),
    ([454,34,12,64,7,33], [7, 12, 33, 34, 64, 454]),
    ([3], [3]),
    ([4,4,5,3,33,66,23,64,23,643534,23,66,4,662], [3, 4, 4, 4, 5, 23, 23, 23, 33, 64, 66, 66, 662, 643534])
]

@pytest.mark.parametrize("input,output", testdata)
def test_cock(input, output):
    assert cocktailShakerSort.cocktailShakerSort(input) == output