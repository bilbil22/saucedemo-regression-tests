# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.page_login import LoginPage
URL = "https://www.saucedemo.com/"


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