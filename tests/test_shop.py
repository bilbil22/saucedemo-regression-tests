URL = "https://www.saucedemo.com/"


def test_end_to_end_purchase(page):
    page.goto(URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click(".shopping_cart_link")

    page.click('[data-test="checkout"]')
    page.fill('[data-test="firstName"]', "Nikola")
    page.fill('[data-test="lastName"]', "Bilbiloski")
    page.fill('[data-test="postalCode"]', "65183")
    page.click('[data-test="continue"]')
    page.click('[data-test="finish"]')

    assert page.url == "https://www.saucedemo.com/checkout-complete.html"
    assert page.locator(".complete-header").inner_text() == "Thank you for your order!"


def test_locked_out_user_cannot_login(page):
    page.goto(URL)
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    error = page.locator('[data-test="error"]')
    assert error.is_visible()
    assert "locked out" in error.inner_text().lower()


def test_add_and_remove_item_updates_cart_badge(page):
    page.goto(URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')
    assert page.locator(".shopping_cart_badge").inner_text() == "2"

    page.click('[data-test="remove-sauce-labs-backpack"]')
    assert page.locator(".shopping_cart_badge").inner_text() == "1"
