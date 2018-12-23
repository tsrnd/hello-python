import pytest, random
from sorting import insertion_sort, selection_sort

total_test_case = 100
min_number = -100000
max_number = 100000
number_of_elements = 10000


def create_test_case():
    test_cases = []
    for _ in range(total_test_case):
        test_case = [
            random.randint(min_number, max_number) for _ in range(number_of_elements)
        ]
        test_cases.append(test_case)
    return test_cases


@pytest.mark.parametrize("input", create_test_case())
# test insertion_sort
def test_insertion_sort(input):
    expect = input.copy()
    expect.sort()
    assert expect == insertion_sort(input)


@pytest.mark.parametrize("input", create_test_case())
# test selection_sort
def test_selection_sort(input):
    expect = input.copy()
    expect.sort()
    assert expect == selection_sort(input)
