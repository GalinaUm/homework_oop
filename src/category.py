from src.product import Product


class Category:
    """Класс, относящий продукт к определенной категории"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(products) if products else 0

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return f'{Product.name}, {Product.price} руб. Остаток: {Product.quantity} шт.'



