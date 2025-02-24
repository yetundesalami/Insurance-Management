class Payment:
    """
    Manages policyholder payments, including processing, reminders, and penalties.
    """
    def __init__(self, policyholder, amount):
        self.policyholder = policyholder
        self.amount = amount
        self.status = "Pending"

    def process_payment(self):
        """Processes the payment and marks it as paid."""
        self.status = "Paid"
        print(f"Payment of ${self.amount} processed for {self.policyholder.name}.")

    def send_reminder(self):
        """Sends a payment reminder if the payment is still pending."""
        if self.status == "Pending":
            print(f"Reminder: {self.policyholder.name}, your payment of ${self.amount} is due.")

    def apply_penalty(self, penalty_amount):
        """Applies a penalty if the payment is overdue."""
        if self.status == "Pending":
            self.amount += penalty_amount
            print(f"Penalty of ${penalty_amount} applied. New amount: ${self.amount}.")
