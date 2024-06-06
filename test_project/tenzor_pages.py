from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_project.interfaces import Refereces

class TenzorPage:
	def __init__(self, urls: str = Refereces.LINK_SBIS):
		self.urls = urls;
		self.run_browser()
		self.found_selector = None

	def run_browser(self) -> None:
		options = Options()
		options.add_argument('--headless')
		self.driver = webdriver.Chrome(options=options) #.Chrome()
		self.driver.set_page_load_timeout(30)

	def open_page_byRef(self) -> None:
		driver = self.driver
		driver.get(self.urls)
		driver.implicitly_wait(0.5)
		self.driver = driver

	def make_click_byElement(self, element) -> None:
		# Here move by the click
		element.click()

	def create_link_forMove(self, selector):
		self.urls = selector.get_attribute('href')
		self.open_page_byRef()

	def find_selector(self, fixture_selector, time=0.5):
		driver = self.driver
		found_selector = None

		if ((self.urls.rfind(Refereces.LINK_TENZOR) >= 0) or (self.urls.rfind(Refereces.LINK_TEMZOR_ABOUT) >= 0)):
			''' Step 3 & 4 & 5'''
			driver.execute_script("window.scrollTo(0, window.innerHeight)")

			if ((fixture_selector[1]).rfind('p a[') >= 0):
				''' ------ 3 & 4------ '''
				try:
					elem = WebDriverWait(driver, timeout=time).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p a[href='/about']")))
					self.urls = elem.get_attribute('href')
					self.open_page_byRef()
					driver = self.driver
					found_selector = driver.current_url
				except Exception as e:
					print(f"Error clicking on element: {e}")

			elif ((fixture_selector[1]).rfind(' img') >= 0):
				''' ------ 5 ------ '''
				try:
					found_selector = WebDriverWait(driver, timeout=time).until(EC.visibility_of_all_elements_located(fixture_selector))
				except Exception as e:
					print(f"Error Image can't found: {e}")

			else:
				found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))
		elif self.urls.rfind(Refereces.LINK_CONTACTS_CHILD) >= 0:
			''' Step 2'''
			try:
				found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))
			except Exception as e:
				print(f"Error - something wrong: {e}")

		elif self.urls.rfind(Refereces.LINK_SBIS) >= 0:
			''' Step 1'''
			try:
				found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))
			except Exception as e:
				print(f"Error Somthing wrong! Element was not found: {e}")
		else:
			''' Step 1'''
			try:
				found_selector = WebDriverWait(driver, timeout=time).until(EC.presence_of_element_located(fixture_selector))
			except Exception as e:
				print(f"Error Somthing wrong! Element was not found: {e}")
		self.driver = driver
		return found_selector

	def teardown_method(self):
		self.driver.close()

	def move_by_link(self, selector):
		self.found_selector = self.find_selector(selector, 20)
		if ((type(self.found_selector) != str) and
			(type(self.found_selector) != list) and
			(bool(self.found_selector.text)) and
			(len(self.found_selector.text) > 0 )):
			text_found = (self.found_selector.text).strip().lower()

		else:
			text_found = (self.found_selector)

		return text_found

		return ''