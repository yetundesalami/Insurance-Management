# policyholder.py
class Policyholder:
    """
    Represents a policyholder in the insurance system.
    Allows registration of insurance products, suspension, and reactivation.
    """
    def __init__(self, policyholder_id, name, status="Active"):
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = status
        self.products = []

    def register_product(self, product):
        """Registers a policyholder for an insurance product if active."""
        if self.status == "Active":
            self.products.append(product)
            print(f"{self.name} registered for product: {product.name}")
        else:
            print(f"Cannot register product. {self.name} is {self.status}.")

    def suspend(self):
        """Suspends the policyholder account."""
        self.status = "Suspended"
        print(f"{self.name} has been suspended.")

    def reactivate(self):
        """Reactivates a suspended policyholder account."""
        self.status = "Active"
        print(f"{self.name} has been reactivated.")
