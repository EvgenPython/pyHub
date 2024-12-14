class Cart:
    def __init__(self):
        self.products = {}

    def __getitem__(self, product):
        return self.products.get(product, 0)

    def __setitem__(self, product, quantity):
        self.products[product] = quantity

    def __delitem__(self, product):
        del self.products[product]

    def add_product(self, product, quantity=1):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity=1):
        if product in self.products:
            if self.products[product] <= quantity:
                del self.products[product]
            else:
                self.products[product] -= quantity


cart = Cart()
print(cart["яблоко"])  # Вывод: 0 (товар отсутствует)
cart.products["яблоко"] = 5
print(cart["яблоко"])  # Вывод: 5

# Ниже расположен код для проверок, его не нужно удалять
cart = Cart()
cart.add_product('Apple', 5)
cart.add_product('Banana')
cart['Orange'] = 3

assert cart['Apple'] == 5, 'Ошибка: метод __getitem__ не возвращает корректное значение для товара "Apple".'
assert cart['Banana'] == 1, 'Ошибка: метод __getitem__ не возвращает корректное значение для товара "Banana".'
assert cart['Orange'] == 3, 'Ошибка: метод __getitem__ не возвращает корректное значение для товара "Orange".'

cart.remove_product('Apple', 2)
assert cart['Apple'] == 3, 'Ошибка: метод __getitem__ не возвращает корректное значение для товара "Apple" после уменьшения количества.'

cart.remove_product('Orange', 3)
assert cart['Orange'] == 0, 'Ошибка: метод __getitem__ не возвращает корректное значение для товара "Orange" после его удаления.'

print('Good')