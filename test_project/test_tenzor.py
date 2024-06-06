from selenium.webdriver.common.by import By
from test_project.tenzor_pages import TenzorPage

class Tenzor:
	SELECTOR_TENZOR_ANCHOR_CONTAT = (By.CSS_SELECTOR, "div.sbisru-Header-sticky li a[href='/contacts']")
	SELECTOR_TENZOR_ANCHOR_BANER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
	SELECTOR_TENZOR_BOX_CONTENT = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title.tensor_ru-pb-16")
	SELECTOR_TENZOR_BOX_CONTENT_LINK = (By.CSS_SELECTOR, "p a[href='/about']")
	SELECTOR_TENZOR_BOX_WORKAHOLICS = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img")


class TestTenzor():
	def setup_method(self) -> None:
		self.tenzor = TenzorPage()


	def test_find_anchor(self):
		''' Step 1'''
		self.tenzor.open_page_byRef()
		text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_ANCHOR_CONTAT)
		extends = "Контакты"

		assert text_found == extends.lower()
		assert text_found.rfind(extends.lower()) >= 0

	def test_find_banner(self):
		''' Step 2'''
		self.tenzor.urls = 'https://sbis.ru/contacts/54-novosibirskaya-oblast'
		self.tenzor.open_page_byRef()
		self.tenzor.driver.implicitly_wait(2)
		self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_ANCHOR_BANER)
		self.tenzor.make_click_byElement(self.tenzor.found_selector)

		''' Step 3'''
		href = self.tenzor.found_selector.get_attribute('href')
		self.tenzor.urls = 'https://tensor.ru/'

		assert href == self.tenzor.urls.lower()
		assert href.rfind(self.tenzor.urls.lower()) >= 0

		href = self.tenzor.found_selector.get_attribute('href')
		self.tenzor.urls = href
		self.tenzor.open_page_byRef()
		if href.rfind(self.tenzor.urls.lower()) >= 0:
			extends = "Сила в людях"

			text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_BOX_CONTENT)


			assert text_found == extends.lower()
			assert text_found.rfind(extends.lower()) >= 0

		if ((self.tenzor.urls).rfind('https://tensor.ru/') >= 0):
			''' Step 4'''
			self.tenzor.urls = 'https://tensor.ru/about'
			self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_BOX_CONTENT_LINK)# assert text_found.rfind(extends.lower()) >= 0

	def test_sizes_ofImg(self):
		if (self.tenzor.urls.rfind('https://tensor.ru/about') >= 0):
			''' Step 5'''
			text_found = self.tenzor.move_by_link(Tenzor.SELECTOR_TENZOR_BOX_WORKAHOLICS)
			if (type(text_found) != list):
				return

			h = text_found[0].size['height']
			w = text_found[0].size['width']
			for img in text_found[1:]:
				assert h == img.size['height']
				assert w == img.size['width']

def test_find_link_contacPage(browser):
		browser.setup_method()
