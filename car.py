from prettytable import PrettyTable
class Car:
    def __init__(self, brand, spare_parts):
        self.brand = brand
        self.spare_parts = spare_parts

    def view_spare_parts(self):
        print(f"{self.brand} Spare Parts:")
        table = PrettyTable()
        table.field_names = ["Part", "Price"]
        for part, price in self.spare_parts.items():
            table.add_row([part, f"${price}"])
        print(table)