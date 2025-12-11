from product import product_details

def test_product_details():
    expected_output = (
        "Product ID: P108\n"
        "Product Name: Moblie\n"
        "Quantity: 5\n"
        "Price: 45000"
    )

    assert product_details("P108", "Moblie", 5, 45000) == expected_output
