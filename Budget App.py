class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):

        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        self.total = 0
        for transaction in self.ledger:
            self.total += transaction["amount"]
        return self.total

    def check_funds(self, amount):

        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({"amount": -amount, "description": description})

        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def __str__(self):
        title = self.name.center(30, "*") + '\n'
        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = f"{transaction['amount']:.2f}"
            title += f"{description:<23}{amount:>7}\n"
        title += f"Total: {self.get_balance():.2f}"
        return title


def create_spend_chart(categories):
    spending = []

    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                total += abs(entry["amount"])
        spending.append(total)

    total_spent = sum(spending)

    percentages = []
    for amount in spending:
        percent = (amount / total_spent) * 100
        percentages.append(int(percent // 10) * 10)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for percent in percentages:
            if percent >= level:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))















