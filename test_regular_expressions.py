import pytest
import re


@pytest.mark.parametrize("test_string,expected", [('A0a', 'A0a'), ('_', '_'),
                                                  ('/', ''), ('@', '')])
def test_string_for_characters(test_string, expected):
    match = re.match(r'\w*', test_string)
    assert match.group(0) == expected


@pytest.mark.parametrize("test_string,expected", [('a', 'a'), ('_', None),
                                                  ('ab', 'ab'), ('abb', 'abb'),
                                                  ('abba', 'abb')])
def test_string_a_followed_by_zero_or_more_b(test_string, expected):
    assert re.match(r'a[b]*', test_string) == expected


if __name__ == '__main__':
    pytest.main()
