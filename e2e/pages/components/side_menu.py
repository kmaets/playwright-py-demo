from playwright.sync_api import Page

class SideMenu:
	def __init__(self, page: Page):
		self.page = page

	def open_side_menu(self):
		self.page.get_by_text(selectors['openMenu']).click()

	def close_side_menu(self):
		self.page.get_by_text(selectors['closeMenu']).click()

	def click_side_menu_link(self, link: str):
		self.open_side_menu()
		match link:
			case 'All Items':
				self.page.get_by_text(selectors['sideMenu']['allItems']).click()
			case 'About':
				self.page.get_by_text(selectors['sideMenu']['about']).click()
			case 'Logout':
				self.page.get_by_text(selectors['sideMenu']['logout']).click()
			case _:
				 print('Element Not Found !!!')

selectors = {
	'sideMenu': {
		'allItems': 'All Items',
		'about': 'About',
		'logout': 'Logout',
		'resetSate': 'Reset App State',
	},
	'openMenu': 'Open Menu',
	'closeMenu': 'password',
	'loginButtonText': 'Login'
}