def test_full_checkout_flow(login_page, inventory_page, cart_page, checkout_page):
    # Login
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.is_loaded()

    # Add item to cart
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    assert inventory_page.get_cart_count() == 1

    # Cart & checkout
    inventory_page.go_to_cart()
    cart_page.click_checkout()

    checkout_page.fill_shipping_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    assert "THANK YOU FOR YOUR ORDER" in checkout_page.get_success_message().upper()
