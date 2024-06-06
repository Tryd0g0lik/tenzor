from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from test_project.interfaces import Refereces, Tenzor
from test_project.tenzor_pages import TenzorPage
import re


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
class TestLocation:

	def check_location(self, selectors=Tenzor.SELECTOR_TENZOR_BOX_LOCATION, extends = 'Новосибирск') -> None:
		found_selector = self.tenzor.find_selector(selectors, 20)
		if ((bool(found_selector.text)) and
			(len(found_selector.text) > 0)):
			text_found = found_selector.text.lower()

			# assert text_found == extends.lower()
			assert text_found.rfind(extends.lower()) >= 0


	def test_manage_location(self):
		self.tenzor = TenzorPage()
		self.tenzor.urls = Refereces.LINK_CONTACTS_CHILD
		self.tenzor.open_page_byRef()
		self.check_location()

		found_selector =  self.tenzor.find_selector(Tenzor.SELECTOR_TENZOR_MANAGE_LOCATION, 20)
		found_selector.click()
		found_selector = self.tenzor.find_selector(Tenzor.SELECTOR_TENZOR_ONE_LOCATION, 20)
		text =found_selector.text

		try:
			# elem = WebDriverWait(self.tenzor.driver, timeout=20).until(EC.element_located_selection_state_to_be((By.CSS_SELECTOR, 'span[title="Камчатский край"] span')))
			actions = ActionChains(self.tenzor.driver)
			actions.move_to_element(found_selector).click().perform()
			WebDriverWait(self.tenzor.driver, 20).until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='СБИС - Камчатка']"))
			)
		except Exception as e:
			print("ERR:",  e)
		result = re.split(r'\d+ ', text )
		if ((len(result[1].split(' ')) > 0) and (len(result[1].split(' ')) > 1)):
			result = [result[1].split(' ')[-2]]



		self.check_location(extends=result[0])
		self.tenzor.driver.close()
