import pytest
from selenium.webdriver.common.by import By

from test_project.tenzor_pages import TenzorPage

class Tenzor:
	SELECTOR_TENZOR_ANCHOR_CONTAT = (By.CSS_SELECTOR, "div.sbisru-Header-sticky li a[href='/contacts']")
	SELECTOR_TENZOR_ANCHOR_BANER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
	SELECTOR_TENZOR_BOX_CONTENT = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title.tensor_ru-pb-16")
	SELECTOR_TENZOR_BOX_CONTENT_LINK = (By.CSS_SELECTOR, "p a[href='/about']")
	SELECTOR_TENZOR_BOX_WORKAHOLICS = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img")


# @pytest.mark.usefixtures("fixture_expected", "fixture_selector")
class TestTenzor():
	def setup_method(self) -> None:
		self.tenzor = TenzorPage()


	# @pytest.mark.skipif(sys.tenzor.urls == "https://sbis.ru/", reason="Skipping test for specific URL")
	def test_find_anchor(self):
		extends: str = ''
		''' Step 1'''
		self.tenzor.open_page_byRef()
		text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_ANCHOR_CONTAT)
		extends = "Контакты"

		assert text_found == extends.lower()
		assert text_found.rfind(extends.lower()) >= 0

		''' Step 2'''
		self.tenzor.urls = 'https://sbis.ru/contacts/54-novosibirskaya-oblast'
		self.tenzor.make_click_byElement(self.tenzor.found_selector)
		self.tenzor.driver.implicitly_wait(2)
		self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_ANCHOR_BANER)
		self.tenzor.make_click_byElement(self.tenzor.found_selector)
		''' Step 3'''
		href = self.tenzor.found_selector.get_attribute('href')
		self.tenzor.urls = 'https://tensor.ru/'

		assert href == self.tenzor.urls.lower()
		assert href.rfind(self.tenzor.urls.lower()) >= 0

		self.tenzor.open_page_byRef()
		if href.rfind(self.tenzor.urls.lower()) >= 0:
			extends = "Сила в людях"

			text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_BOX_CONTENT)
			self.tenzor.driver.implicitly_wait(2)

			assert text_found == extends.lower()
			assert text_found.rfind(extends.lower()) >= 0

		if ((self.tenzor.urls).rfind('https://tensor.ru/') >= 0):
			''' Step 4'''
			self.tenzor.urls = 'https://tensor.ru/about'
			self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_BOX_CONTENT_LINK)# assert text_found.rfind(extends.lower()) >= 0

		if (self.tenzor.urls.rfind('https://tensor.ru/about') >= 0):
			''' Step 5'''
			# self.tenzor.urls = 'https://tensor.ru/about'
			# resultJS = self.tenzor.driver.execute_script("document.querySelectorAll('.tensor_ru-Index__block4-bg p')[document.querySelectorAll('.tensor_ru-Index__block4-bg p').length - 1]")
			text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_BOX_WORKAHOLICS)
			assert text_found == extends.lower()
			assert text_found.rfind(extends.lower()) >= 0


def test_find_link_contacPage(browser):
		browser.setup_method()
