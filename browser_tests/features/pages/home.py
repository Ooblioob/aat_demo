from pages.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Home(Base):
	LOVE_IT_BUTTON_XPATH = "//button[text()='Love it']"
	CAT_IMAGE_ID = "main_event"

	def __init__(self, logger, directory, base_url=r'http://localhost/',
				 driver=None, driver_wait=10, delay_secs=0):
		super(Home, self).__init__(logger, directory, base_url,
								   driver, driver_wait, delay_secs)

	def go(self):
		super(Home, self).go()

	def get_love_it_button(self):
		return self.driver.find_element_by_xpath(self.LOVE_IT_BUTTON_XPATH)

	def get_cat_image(self):
		return self.driver.find_element_by_id(self.CAT_IMAGE_ID)

	def get_cat_image_src(self):
		return self.get_cat_image().get_attribute("src")

	def wait_for_image_to_reload(self, current_img):
		self.wait().until(lambda ec: self.get_cat_image_src() != current_img)
