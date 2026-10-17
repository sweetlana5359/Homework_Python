import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ('anna', 'Anna'),
    ('silly cat', 'Silly cat'),
    ('t-shirt', 'T-shirt'),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ('', ''),
    ('2378', '2378'),
    ('  ', '  '),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    (' Marry', 'Marry'),
    (' Rio de Janeiro', 'Rio de Janeiro'),
    (' Lesson ', 'Lesson '),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('', ''),
    (' 3456', '3456'),
    (' !@#', '!@#'),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol, expected', [
    ('Panda', 'n', True),
    ('Marry Jane', 'J', True),
    ('33 cows', 'w', True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol, expected', [
    ('Leaves', 'n', False),
    ('', 'z', False),
    ('Hakuna Matata', 'K', False),
    ('@#$', 'y', False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol, expected', [
    ('Alice', 'i', 'Alce'),
    ('New York', 'New', ' York'),
    ('#cool', '#', 'cool'),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol, expected', [
    ('', 'd', ''),
    ('5748', 'yes', '5748'),
    ('#@$', '!', '#@$'),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
