import pytest
import re


@pytest.mark.parametrize("test_string,expected", [('A0a', 'A0a'), ('_', '_'),
                                                  ('/', ''), ('@', '')])
def test_string_for_characters(test_string, expected):
    match = re.match(r'\w*', test_string)
    assert match.group(0) == expected


if __name__ == '__main__':
    pytest.main()
