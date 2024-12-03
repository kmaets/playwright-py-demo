import re
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.components.side_menu import SideMenu

from fixtures.set_testid import setup_test_id_attribute

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each():
	print('before the test runs')
	setup_test_id_attribute
	yield
	print('after the test runs')
	
def test_open_swag_login_page(page: Page):
	page.goto('https://www.saucedemo.com/')
	expect(page).to_have_title(re.compile('Swag Labs'))

@pytest.mark.login
def test_login_with_valid_credentials(page: Page):
	login_page = LoginPage(page)
	side_menu = SideMenu(page)

	page.goto('https://www.saucedemo.com/')
	login_page.login('standard_user', 'secret_sauce')
	expect(page).to_have_url(re.compile('https://www.saucedemo.com/inventory'))

	side_menu.click_side_menu_link('Logout')

def test_login_with_invalid_credentials(page: Page):
	login_page = LoginPage(page)

	page.goto('https://www.saucedemo.com/')
	login_page.login('fake_user', 'secret_sauce')
	expect(login_page.get_login_error_element()).to_be_visible()
	expect(login_page.get_login_error_element()).to_contain_text('Username and password do not match')

