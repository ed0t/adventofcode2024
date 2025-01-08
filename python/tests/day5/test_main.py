from day5.main import load, validate, validate_all, validate_with_reordering
import pytest

input = """47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13
    """


# 75, 47, 61, 53, 29
# 97, 61, 53, 29, 13
# 75, 29, 13
# 75, 97, 47, 61, 53
# 61, 13, 29
# 97, 13, 75, 29, 47


def test_main_is_correct():
    rules, updates = load("./day5/sample_input.txt")
    assert validate(rules, [75, 47, 61, 53, 29]) == 61
    assert validate(rules, [97, 61, 53, 29, 13]) == 53
    assert validate(rules, [75, 29, 13]) == 29


def test_main_is_not_correct():
    rules, updates = load("./day5/sample_input.txt")
    assert validate(rules, [75, 97, 47, 61, 53]) is None
    assert validate(rules, [61, 13, 29]) is None
    assert validate(rules, [97, 13, 75, 29, 47]) is None

def test_main_against_all_updates():
    rules, updates = load("./day5/sample_input.txt")

    assert validate_all(rules, updates) == 143

def test_main_correct_unordered():
    rules, updates = load("./day5/sample_input.txt")

    # print(rules)
    assert validate_with_reordering(rules, [75, 97, 47, 61, 53]) is 47
    assert validate_with_reordering(rules, [61, 13, 29]) is 29
    assert validate_with_reordering(rules, [97, 13, 75, 29, 47]) is 47

    assert validate_all(rules, [[75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]) == (0, 123)
