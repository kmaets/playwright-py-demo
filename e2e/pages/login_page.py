from playwright.sync_api import sync_playwright, Page

class LoginPage:
	def __init__(self, page: Page):
		self.page = page

	def enter_username(self, username: str):
		self.page.get_by_test_id('username').fill(username)

	def enter_password(self, password: str):
		self.page.get_by_test_id('password').fill(password)

	def click_login(self):
		self.page.get_by_text('Login').click()

	def login(self, username: str, password: str):
		self.enter_username(username)
		self.enter_password(password)
		self.click_login()

with sync_playwright() as playwright:
    playwright.selectors.set_test_id_attribute('data-test')