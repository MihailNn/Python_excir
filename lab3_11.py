# Создать класс Product: id, Наименование, UPC, Производитель, Цена,
# Срок хранения, Количество.
# Функции-члены реализуют запись и считывание полей (проверка корректности),
# вывод общей суммы продукта.
# Создать список объектов. Вывести:
# a)	список товаров для заданного наименования;
# b)	список товаров для заданного наименования, цена которых не превосходит заданную;
class Product:
    def __init__(self, prod_id, title, upc, manufacturer, price, expiry_date, quantity):
        self.id = prod_id
        self.title = title
        self.upc = upc
        self.manufacturer = manufacturer
        self.price = price
        self.expiry_date = expiry_date
        self.quantity = quantity

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def get_upc(self):
        return self.upc

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date

    def get_expiry_date(self):
        return self.expiry_date

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def sum_product(self):
        return self.price * self.quantity

    def __setattr__(self, attr, value):
        if attr != id:
            self.__dict__[attr] = value
        else:
            raise AttributeError

    # def print_products(self):
    #     for obj in self:
    #         print(obj.get_title(), '  ', obj.get_manufacturer())
    #     return


product_list = [
    Product('3453', 'ice-cream', '220092', 'mestnoye izvestnoye', '1.28', '20-04-2021', '100'),
    Product('3454', 'milk', '220092', 'mestnoye izvestnoye', '1.63', '20-03-2021', '120'),
    Product('3455', 'cheese', '220092', 'Gorki', '9.37', '27-04-2021', '50'),
    Product('3457', 'cottage cheese', '220092', 'mestnoye izvestnoye', '1.79', '07-03-2021', '130'),
    Product('3459', 'yogurt', '220092', 'Gorki', '1.53', '12-04-2021', '110'),
]

def print_list(obj_list, param):
    if len(obj_list) > 0:
        print(f'Result by "{param}":')
        for obj in obj_list:
            print(obj.get_title(), ' : ', obj.get_manufacturer(), ' : ', obj.get_price())
        return


def show_result(arg, lambda_exp):
    filter_result = list(filter(lambda_exp, product_list))
    print_list(filter_result, arg) if len(filter_result) > 0 else print('No data')


manufacturer_request = input('Input manufacturer: \n')
show_result(manufacturer_request, lambda x: x.get_manufacturer() == manufacturer_request)

price_request = input('Input price: ')
show_result(price_request, lambda x: x.get_price() > price_request)
