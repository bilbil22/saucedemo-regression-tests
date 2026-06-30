# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.page_login import LoginPage
import pytest

URL = "https://www.saucedemo.com/"

@pytest.mark.e2e
def test_end_to_end_purchase(page):

    login_page = LoginPage(page)

    login_page.navigate(URL)
    login_page.login("standard_user", "secret_sauce")

    login_page.add_backpack_to_cart()
    login_page.open_cart()

    login_page.checkout(
        "Nikola",
        "Bilbiloski",
        "65183"
    )

    login_page.finish_order()

    assert page.url == "https://www.saucedemo.com/checkout-complete.html"
    assert login_page.get_complete_message() == "Thank you for your order!"

    
@pytest.mark.smoke
def test_locked_out_user_cannot_login(page):
    login_page = LoginPage(page)

    login_page.navigate(URL)
    login_page.login("locked_out_user", "secret_sauce")

    error = page.locator('[data-test="error"]')
    assert error.is_visible()
    assert "locked out" in error.inner_text().lower()
    # page.wait_for_timeout(5000)  # Pause to visually confirm the error message


@pytest.mark.sanity
def test_add_and_remove_item_updates_cart_badge(page):
    login_page = LoginPage(page)

    login_page.navigate(URL)
    login_page.login("standard_user", "secret_sauce")

    login_page.add_backpack_to_cart()
    login_page.add_bike_light_to_cart()
    assert login_page.get_cart_item_count() == "2"

    login_page.remove_backpack_from_cart()
    assert login_page.get_cart_item_count() == "1"


