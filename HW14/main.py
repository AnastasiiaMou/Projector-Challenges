# Task1


# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


# class Book(Product):
#     def __init__(self, name, price, quantity, author):
#         super().__init__(name, price, quantity)
#         self.author = author

#     def read(self):
#         print(f"Reading the book {self.name} by {self.author}")


# book1 = Book("Harry Potter", 20, 9, "Rowling")
# book1.read()


# Task 2
# class Restaurant:
#     def __init__(self, name, cuisine, menu):
#         self.name = name
#         self.cuisine = cuisine
#         self.menu = menu

#     def order(self, dish_name, quantity):
#         if dish_name in self.menu and quantity <= self.menu[dish_name]["quantity"]:
#             total_cost = self.menu[dish_name]["price"] * quantity
#             self.menu[dish_name]["quantity"] -= quantity
#             return total_cost
#         elif dish_name in self.menu and quantity > self.menu[dish_name]["quantity"]:
#             return "Sorry, requested quantity is not avalable"
#         else:
#             return "Sorry, requested dish is not available"


# class FastFood(Restaurant):
#     def __init__(self, name, cuisine, menu, drive_thru):
#         super().__init__(name, cuisine, menu)
#         self.drive_thru = drive_thru


# menu = {
#     "burger": {"price": 5, "quantity": 10},
#     "pizza": {"price": 10, "quantity": 20},
#     "drink": {"price": 1, "quantity": 15},
# }

# mc = FastFood("McDonalds", "Fast Food", menu, True)

# print(mc.order("burger", 5))  # 25
# print(mc.order("burger", 15))  # Requested quantity not available
# print(mc.order("soup", 5))  # Dish not available


# Task 3
class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Amount must be positive")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account number: {self._account_number}, balance: {self._balance}"


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

        def add_interest(self):
            self.balance += self.balance * self.interest


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit


class Bank:
    def __init__(self):
        self.accounts = []

        def open_account(self, account):
            self.accounts.appent(account)

        def close_account(self, account_number):
            self.account = [
                account
                for account in self.accounts
                if account.get_account_number() != account_number
            ]

        def pay_div(self, amount):
            for account in self.accounts:
                account.deposit(amount)

        def update(self):
            for account in self.accounts:
                if isinstance(account, SavingsAccount):
                    account.add_interest()
                elif isinstance(account, CurrentAccount) and account.get_balance() < 0:
                    print("YOu are overdraft")


savings_account1 = SavingsAccount(1000, "SA001", 0.05)
print(savings_account1)
current_account1 = CurrentAccount(500, "CA001", -500)
print(current_account1)
