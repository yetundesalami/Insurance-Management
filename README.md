# Insurance Policy Management System

## Overview
This project is an Insurance Policy Management System designed to manage policyholders, insurance products, and payments. The system allows policy managers to register, suspend, and reactivate policyholders, manage insurance products, and handle payment processing.

## Features
- **Policyholder Management**: Register, suspend, and reactivate policyholders.
- **Product Management**: Create, update, and suspend insurance products.
- **Payment Management**: Process payments, send reminders, and apply penalties.

## File Structure
- `policyholder.py`: Defines the `Policyholder` class for managing policyholders.
- `product.py`: Defines the `Product` class for managing insurance products.
- `payment.py`: Defines the `Payment` class for handling payments.
- `main.py`: Demonstrates the functionality by creating policyholders, assigning products, and processing payments.

## Installation & Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   cd insurance-policy-management
   ```
2. Ensure you have Python installed (version 3.x recommended).
3. Run the `main.py` file to test the system:
   ```
   python main.py
   ```

## Usage
- The `Policyholder` class allows registering products, suspending, and reactivating policyholders.
- The `Product` class allows updating product prices and suspending products.
- The `Payment` class handles processing payments, sending reminders, and applying penalties.
- Running `main.py` will create policyholders, register them to products, process payments, and display their details.

## Example Output
```
Rex registered for product: Health Insurance
Tony registered for product: Life Insurance
Payment of $500 processed for Rex.
Payment of $300 processed for Tony.
Rex has Active status with 1 products.
Tony has Active status with 1 products.
```

## Author
Yetunde Salami

