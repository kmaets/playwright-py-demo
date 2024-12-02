import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.components.side_menu import SideMenu

def test_login_with_valid_credentials(page: Page):
        login_page = LoginPage(page)
        side_menu = SideMenu(page)

        page.goto('https://www.saucedemo.com/')
        login_page.login('standard_user', 'secret_sauce')
        expect(page).to_have_url(re.compile('https://www.saucedemo.com/inventory'))

        side_menu.click_side_menu_link('Logout')
