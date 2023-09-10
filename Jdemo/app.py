class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.shopping_cart = ShoppingCart()

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        # Simulate payment processing here
        return total

# Test Cases
import unittest

class TestECommerce(unittest.TestCase):
    def test_add_to_cart(self):
        product = Product(1, "Product A", 10.0)
        user = User("user1", "user1@example.com")
        user.shopping_cart.add_item(product, quantity=2)
        self.assertEqual(len(user.shopping_cart.items), 1)

    def test_remove_from_cart(self):
        product = Product(1, "Product A", 10.0)
        user = User("user1", "user1@example.com")
        user.shopping_cart.add_item(product, quantity=2)
        user.shopping_cart.remove_item(product)
        self.assertEqual(len(user.shopping_cart.items), 0)

    def test_calculate_total(self):
        product1 = Product(1, "Product A", 10.0)
        product2 = Product(2, "Product B", 15.0)
        user = User("user1", "user1@example.com")
        user.shopping_cart.add_item(product1, quantity=2)
        user.shopping_cart.add_item(product2, quantity=3)
        total = user.shopping_cart.calculate_total()
        self.assertEqual(total, 2 * 10.0 + 3 * 15.0)

if __name__ == "__main__":
    unittest.main()

