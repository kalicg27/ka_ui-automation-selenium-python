def test_valid_login(login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded()


def test_invalid_password(login_page):
    login_page.login("standard_user", "wrong_password")
    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message or "Epic sadface" in error_message


def test_locked_out_user(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    error_message = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error_message
