# Linear Test Automation Framework or Script-Based Test Automation for SauceDemo using Playwright and Pytest
import pytest

URL = "https://www.saucedemo.com/"

@pytest.mark.e2e
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


@pytest.mark.smoke
def test_locked_out_user_cannot_login(page):
    page.goto(URL)
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    error = page.locator('[data-test="error"]')
    assert error.is_visible()
    assert "locked out" in error.inner_text().lower()
    # page.wait_for_timeout(5000)  # Pause to visually confirm the error message


@pytest.mark.sanity
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


    # Refactoring of the test_shop.py to use the Page Object Model (POM) design pattern. The test_login.py utilizes the Page Object Model to encapsulate the login functionality, making the test more readable and maintainable.