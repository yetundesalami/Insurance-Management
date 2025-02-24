# product.py
class Product:
    """
    Represents an insurance product with a name, price, and availability status.
    """
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = "Available"

    def update_price(self, new_price):
        """Updates the price of the insurance product."""
        self.price = new_price
        print(f"Price of {self.name} updated to {self.price}.")

    def suspend(self):
        """Suspends the insurance product."""
        self.status = "Suspended"
        print(f"Product {self.name} has been suspended.")