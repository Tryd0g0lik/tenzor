import pytest
from selenium.webdriver.common.by import By

from test_project.test_tenzor import TestTenzor

# @pytest.fixture
# def fixture_expected():
# 	for elem in ["Контакты", "Сила в людях"]:
# 		yield elem
# @pytest.fixture
# def fixture_selector():
# 	for elem in [Tenzor.SELECTOR_TENZOR_ANCHOR_CONTAT,
# 	            Tenzor.XPATH_TENZOR_ANCHOR_BANER]:
# 		yield elem

@pytest.fixture(scope='class')
def browser():
	tenzor = TestTenzor()
	return tenzor
