# POM (Page Object Model) for the login page of the SauceDemo application using Playwright and Pytest. This class encapsulates the login functionality, making the test more readable and maintainable.
# from curses import error

from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page   

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
    # New Class Methods for Shopping Actions
    def add_backpack_to_cart(self):
        self.page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
        

    def add_bike_light_to_cart(self):
        self.page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')   
    
    def open_cart(self):
        self.page.click(".shopping_cart_link")
    # New Class Methods for Checkout Actions
    def checkout(self, first_name, last_name, postal_code):
        self.page.click('[data-test="checkout"]')
        self.page.fill('[data-test="firstName"]', first_name)
        self.page.fill('[data-test="lastName"]', last_name)
        self.page.fill('[data-test="postalCode"]', postal_code)
        self.page.click('[data-test="continue"]')

    def get_cart_item_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()
    
    def remove_backpack_from_cart(self):
        self.page.click('[data-test="remove-sauce-labs-backpack"]')

    def finish_order(self):
        self.page.click('[data-test="finish"]')

    def get_complete_message(self):
        return self.page.locator(".complete-header").inner_text()
    # Login Error Handling
    def get_error_message(self):
        error = self.page.locator('[data-test="error"]')
        # return error.inner_text() if error.is_visible() else None
        assert error.is_visible()
        assert "locked out" in error.inner_text().lower()