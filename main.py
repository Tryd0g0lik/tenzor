import pytest

from test_project.test_tenzor import TestTenzor


if __name__ == '__main__':
    pytest.main(["-v", "--color=yes", "./test_project/test_tenzor.py"])


