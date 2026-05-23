from pages.login_page import LoginPage
from config import config


def test_successful_login(setup_browser):

    page = setup_browser

    login_page = LoginPage(page)

    login_page.load()

    login_page.login(
        config.VALID_USERNAME,
        config.VALID_PASSWORD
    )

    page.wait_for_timeout(5000)

    assert "dashboard" in page.url.lower()


def test_unsuccessful_login(setup_browser):

    page = setup_browser

    login_page = LoginPage(page)

    login_page.load()

    login_page.login(
        "wrong@gmail.com",
        "wrongpassword"
    )

    assert "login" in page.url.lower()