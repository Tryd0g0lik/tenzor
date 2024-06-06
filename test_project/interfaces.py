from selenium.webdriver.common.by import By


class Tenzor:
	SELECTOR_TENZOR_ANCHOR_CONTAT = (By.CSS_SELECTOR, "div.sbisru-Header-sticky li a[href='/contacts']")
	SELECTOR_TENZOR_ANCHOR_BANER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
	SELECTOR_TENZOR_BOX_CONTENT = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title.tensor_ru-pb-16")
	SELECTOR_TENZOR_BOX_CONTENT_LINK = (By.CSS_SELECTOR, "p a[href='/about']")
	SELECTOR_TENZOR_BOX_WORKAHOLICS = (By.CSS_SELECTOR, ".tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 img")
	SELECTOR_TENZOR_BOX_LOCATION = (By.CSS_SELECTOR, ".sbisru-Contacts-City__item-name.sbisru-link.pr-4")
	SELECTOR_TENZOR_MANAGE_LOCATION = (By.CSS_SELECTOR, ".s-Grid-col.s-Grid-col--xm12 span.sbis_ru-Region-Chooser__text.sbis_ru-link")
	SELECTOR_TENZOR_ONE_LOCATION = (By.CSS_SELECTOR, 'span[title="Камчатский край"] span')

class Refereces:
	LINK_CONTACTS_CHILD = 'https://sbis.ru/contacts/54-novosibirskaya-oblast'
	LINK_TENZOR = 'https://tensor.ru/'
	LINK_TEMZOR_ABOUT = 'https://tensor.ru/about'
	LINK_SBIS = 'https://sbis.ru'