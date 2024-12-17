from datetime import datetime

class Cart:
    def __init__(self, cart_id, user_id):
        self.cart_id = cart_id
        self.user_id = user_id
        self.items = []
        self.total = 0.0

    def add_product(self, product, quantity):
        if quantity <= 0:
            raise ValueError("The quantity must be greater than 0")
        for item in self.items:
            if item['product_id'] == product['id']:
                item['quantity'] += quantity
                self.calculate_total()
                return
        self.items.append({
            'product_id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity
        })
        self.calculate_total()

    def delete_product(self, product_id):
        self.items = [item for item in self.items if item['product_id'] != product_id]
        self.calculate_total()

    def update_quantity(self, product_id, new_quantity):
        if new_quantity < 0:
            raise ValueError("The quantity must not be negative.")
        for item in self.items:
            if item['product_id'] == product_id:
                item['quantity'] = new_quantity
                self.calculate_total()
                return
        raise ValueError("The product was not found in the cart.")

    def calculate_total(self):
        self.total = sum(item['price'] * item['quantity'] for item in self.items)
        return self.total

    def clear_cart(self):
        self.items = []
        self.total = 0.0

    def get_items(self):
        return self.items


class Order:
    def __init__(self, order_id, cart, state="Pending", date=None):
        self.order_id = order_id
        self.cart = cart
        self.state = state
        self.date = date if date else datetime.now()

    def confirm_order(self):
        self.state = "Confirmed"

    def cancel_order(self):
        self.state = "Canceled"

    def get_order_details(self):
        return {
            "order_id": self.order_id,
            "user_id": self.cart.user_id,
            "items": self.cart.get_items(),
            "total": self.cart.total,
            "state": self.state,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
        }


class Payment:
    def __init__(self, payment_id, order, amount, method, state="Pending", date=None):
        if amount <= 0:
            raise ValueError("The amount must be greater than 0.")
        if method not in ["Card", "PayPal", "Transfer"]:
            raise ValueError("Invalid payment method.")
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.method = method
        self.state = state
        self.date = date if date else datetime.now()

    def confirm_payment(self):
        self.state = "Approved"
        self.order.state = "Paid"

    def decline_payment(self):
        self.state = "Refused"

