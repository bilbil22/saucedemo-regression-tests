from playwright.sync_api import Page   

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def add_backpack_to_cart(self):
        self.page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

    def open_cart(self):
        self.page.click(".shopping_cart_link")

    def checkout(self, first_name, last_name, postal_code):
        self.page.click('[data-test="checkout"]')
        self.page.fill('[data-test="firstName"]', first_name)
        self.page.fill('[data-test="lastName"]', last_name)
        self.page.fill('[data-test="postalCode"]', postal_code)
        self.page.click('[data-test="continue"]')

    def finish_order(self):
        self.page.click('[data-test="finish"]')

    def get_complete_message(self):
        return self.page.locator(".complete-header").inner_text()