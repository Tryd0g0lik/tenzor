import pytest
from selenium.webdriver.common.by import By

from test_project.tenzor_pages import TenzorPage

class Tenzor:
	SELECTOR_TENZOR_ANCHOR_CONTAT = (By.CSS_SELECTOR, "div.sbisru-Header-sticky li a[href='/contacts']")
	SELECTOR_TENZOR_ANCHOR_BANER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
	SELECTOR_TENZOR_BOX_CONTENT = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title.tensor_ru-pb-16")


# @pytest.mark.usefixtures("fixture_expected", "fixture_selector")
class TestTenzor():
	def setup_method(self) -> None:
		self.tenzor = TenzorPage()


	# @pytest.mark.skipif(sys.tenzor.urls == "https://sbis.ru/", reason="Skipping test for specific URL")
	def test_find_anchor(self):
		extends: str = ''
		# if self.tenzor.urls == "https://sbis.ru/":
		self.tenzor.open_page_byRef()
		text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_ANCHOR_CONTAT)
		extends = "Контакты"

		assert text_found == extends.lower()
		assert text_found.rfind(extends.lower()) >= 0

		# self.tenzor.found_selector

		self.tenzor.urls = 'https://sbis.ru/contacts/54-novosibirskaya-oblast'
		self.tenzor.make_click_byElement(self.tenzor.found_selector)
		self.tenzor.driver.implicitly_wait(2)
		self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_ANCHOR_BANER)
		self.tenzor.make_click_byElement(self.tenzor.found_selector)
		href = self.tenzor.found_selector.get_attribute('href')
		self.tenzor.urls = 'https://tensor.ru/'

		assert href == self.tenzor.urls.lower()
		assert href.rfind(self.tenzor.urls.lower()) >= 0


		if href.rfind(self.tenzor.urls.lower()) >= 0:
			self.tenzor.open_page_byRef()
			extends = "Сила в людях"

			text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_BOX_CONTENT)
			self.tenzor.driver.implicitly_wait(2)

			assert text_found == extends.lower()
			assert text_found.rfind(extends.lower()) >= 0









def test_find_link_contacPage(browser):
		browser.setup_method()
