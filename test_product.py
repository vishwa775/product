from product import product

def test_product():
    expected_output = (
        "Product ID: P108\n"
        "Product Name: Moblie\n"
        "Quantity: 5\n"
        "Price: 45000"
    )

    assert product("P108", "Moblie", 5, 45000) == expected_output
