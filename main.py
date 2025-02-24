# main.py
from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
product1 = Product(1, "Health Insurance", 500)
product2 = Product(2, "Life Insurance", 300)

# Create policyholders
policyholder1 = Policyholder(101, "Rex")
policyholder2 = Policyholder(102, "Tony")

# Register products
policyholder1.register_product(product1)
policyholder2.register_product(product2)

# Process payments
payment1 = Payment(policyholder1, product1.price)
payment2 = Payment(policyholder2, product2.price)

payment1.process_payment()
payment2.process_payment()

# Display account details
print(f"{policyholder1.name} has {policyholder1.status} status with {len(policyholder1.products)} products.")
print(f"{policyholder2.name} has {policyholder2.status} status with {len(policyholder2.products)} products.")