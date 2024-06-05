from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TenzorPage:
	def __init__(self, urls: str = 'https://sbis.ru/'):
		self.urls = urls;
		self.run_browser()
		self.found_selector = None

	def run_browser(self) -> None:
		# options = Options()
		# options.add_argument('--headless')
		self.driver = webdriver.Chrome() #.Chrome(options=options) #.Chrome()

	def open_page_byRef(self) -> None:
		driver = self.driver
		driver.get(self.urls)
		driver.implicitly_wait(0.5)
		self.driver = driver

	def make_click_byElement(self, element) -> None:
		# Here move by the click
		element.click()

	def find_selector(self, fixture_selector, time=0.5):
		driver = self.driver
		driver.implicitly_wait(time)
		found_selector = None

		if self.urls.rfind('https://tensor.ru/') >= 0:
			driver.execute_script("window.scrollTo(0, window.innerHeight)")
			# found_selector = WebDriverWait(driver, 10).until(
			# 	EC.presence_of_element_located(*fixture_selector)
			# )
			found_selector = driver.find_element(*fixture_selector)

			# found_selector = driver.find_element(*fixture_selector)
			# (By.CLASS_NAME, "p.tensor_ru-Index__card-title.tensor_ru-pb-16")
		if self.urls.rfind('https://sbis.ru/contacts/54-novosibirskaya-oblast') >= 0:
			found_selector = driver.find_element(*fixture_selector)




		if self.urls.rfind('https://sbis.ru/') >= 0:
			found_selector = driver.find_element(*fixture_selector)

		driver.implicitly_wait(time)
		self.driver = driver
		return  found_selector

	def teardown_method(self):
		self.driver.close()

	def move_by_link(self, selector):
		self.found_selector = self.find_selector(selector)
		if (len(self.found_selector.text) > 0 ):
			text_found = (self.found_selector.text
			              .strip()
			              .lower())
			return text_found

		return ''