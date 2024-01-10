class Products:

    def __init__(self, company, **kw):
        self.company = company
        self.model = kw.get("model")
        self.price = kw.get("price")
        self.is_stocked = True

def check_stocked(function):
    def wrapper(**kw):
        com = kw.get("com")
        if com.is_stocked:
            function(com)
    return wrapper

@check_stocked
def available_products(product):
    print(f"company: {product.company}\n"
          f"model: {product.model}\n"
          f"price: {product.price}")

antelope = Products(company="Antelope", model="goliath", price="1,000,000")
available_products(com=antelope)
