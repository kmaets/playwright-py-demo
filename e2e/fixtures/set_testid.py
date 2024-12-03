import pytest

@pytest.fixture(autouse=True)
def setup_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute('data-test')