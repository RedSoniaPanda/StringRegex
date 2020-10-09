import pytest
import re


@pytest.mark.parametrize("test_string,expected", [('A0a', 'A0a'), ('_', '_'),
                                                  ('/', ''), ('@', '')])
def test_string_for_characters(test_string, expected):
    match = re.match(r'\w*', test_string)
    assert match.group(0) == expected


@pytest.mark.parametrize("test_string,expected", [('a', 'a'), ('_', ''),
                                                  ('abb', 'abb'), ('cb', ''),
                                                  ('abbc', 'abb'), ('abba', 'abb'),
                                                  ('.', '')])
def test_string_a_followed_by_zero_or_more_b(test_string, expected):
    match = re.match(r'ab*', test_string)
    if not match:
        assert '' == expected
    else:
        assert match.group(0) == expected


@pytest.mark.parametrize("test_string,expected", [('a', ''), ('_', ''),
                                                  ('abb', 'abb'), ('cb', ''),
                                                  ('abbc', 'abb'), ('abba', 'abb'),
                                                  ('.', '')])
def test_string_a_followed_by_one_or_more_b(test_string, expected):
    match = re.match(r'ab+', test_string)
    if not match:
        assert '' == expected
    else:
        assert match.group(0) == expected


if __name__ == '__main__':
    pytest.main()
