from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener as AL
from selenium.webdriver.support import expected_conditions as EC
import json
class TenzorPage:
	def __init__(self, urls: str = 'https://sbis.ru/'):
		self.urls = urls;
		self.run_browser()
		self.found_selector = None

	def run_browser(self) -> None:
		options = Options()
		options.add_argument('--headless')
		self.driver = webdriver.Chrome(options=options) #.Chrome()

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
		found_selector = None

		if ((self.urls.rfind('https://tensor.ru/') >= 0) or (self.urls.rfind('https://tensor.ru/about') >= 0)):
			''' Step 3 & 4 & 5'''
			hsize = 0
			wsize = 0
			driver.execute_script("window.scrollTo(0, window.innerHeight)")
			# driver.implicitly_wait(time)
			# found_selector = driver.find_elements(*fixture_selector)
			# found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))

			#and (found_selector[len(found_selector) - 1].text.rfind('Подробнее') >= 0)
			if ((fixture_selector[1]).rfind('p a[') >= 0):
				''' ------ 3 & 4------ '''
				# driver.implicitly_wait(time)
				# self.make_click_byElement(found_selector[len(found_selector) - 1])
				# driver.find_elements(*fixture_selector)[0].click()
				# self.make_click_byElement(found_selector)
				# driver.implicitly_wait(time)
				try:
					# wait = WebDriverWait(driver, timeout=time)
					driver.execute_script("window.scrollTo(0, window.innerHeight)")
					# found_selector = wait.until(EC.presence_of_element_located(fixture_selector)) .element_to_be_clickable
					# wait.until(EC.presence_of_element_located(fixture_selector))
					# (driver.find_element(*fixture_selector)).click()
					elem = WebDriverWait(driver, timeout=time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p a[href='/about']")))
					self.urls = elem.get_attribute('href')
					self.open_page_byRef()
					driver = self.driver
					found_selector = driver.current_url
				except Exception as e:
					print(f"Error clicking on element: {e}")

				# found_selector = driver.current_url
				# if ((type(found_selector) == str) and (found_selector.text.rfind('Подробнее') >= 0)):
				# if (type(found_selector) == str):



			elif ((fixture_selector[1]).rfind(' img') >= 0):
				''' ------ 5 ------ '''
				for img in found_selector:
					img
			else:
				# found_selector = found_selector[len(found_selector) - 1]
				found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))
			# found_selector = driver.find_element(*fixture_selector)
			# (By.CLASS_NAME, "p.tensor_ru-Index__card-title.tensor_ru-pb-16")
		elif self.urls.rfind('https://sbis.ru/contacts/54-novosibirskaya-oblast') >= 0:
			''' Step 2'''
			# found_selector = driver.find_element(*fixture_selector)
			found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))

		elif self.urls.rfind('https://sbis.ru/') >= 0:
			''' Step 1'''
			found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))

		self.driver = driver
		return found_selector

	def teardown_method(self):
		self.driver.close()

	def move_by_link(self, selector):
		self.found_selector = self.find_selector(selector, 10)
		text_found = ''
		if (type(self.found_selector) != str ) and (len(self.found_selector.text) > 0 ):
			text_found = (self.found_selector.text).strip().lower()
		else:
			text_found = (self.found_selector)

		return text_found

		return ''