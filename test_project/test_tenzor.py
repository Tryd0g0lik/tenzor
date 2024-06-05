import pages as pages
import self as self
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest

class Tenzor:
	SELECTOR_TENZOR_ANCHOR_CONTAT = (By.CSS_SELECTOR, "div.sbisru-Header-sticky li a[href='/contacts']")

class TenzorPage:
	def __init__(self, urls: str = 'https://sbis.ru/'):
		self.urls = urls;
		self.run_browser()

	def run_browser(self):
		# options = Options()
		# options.add_argument('--headless')
		self.driver = webdriver.Chrome()  # .Chrome(options=options)

	def open_page_byRef(self, browser):  # test_bannerTenzor_of_mainPage test_find_link_contacPage
		driver = browser
		driver.get(self.urls)
		driver.implicitly_wait(0.5)
		self.driver = driver

class TestTenzor(TenzorPage):
	def __init__(self):
		super().__init__()
		self.time = 2

	def test_find_anchor(self, expected:str, time=0.5):
		self.open_page_byRef(self.driver)
		find_selector = Tenzor.SELECTOR_TENZOR_ANCHOR_CONTAT

		driver = self.driver
		found_selector = driver.find_element(*find_selector)
		driver.implicitly_wait(time)
		self.driver = driver


		text_of_anchor =  (found_selector.text
		          .strip()
		          .lower()) #.rfind(expected.lower())

		assert text_of_anchor == expected.lower()
		assert text_of_anchor in expected.lower()

	def close_test(self):
		self.driver.close()
	# def test_find_link_contacPage(self, browser):



