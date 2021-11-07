# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

name_1 = input("Введите наименование товара: ")
price_1 = input("Введите цену товара: ")
amount_1 = input("Введите кол-во товара: ")

dict_product1 = {"Наименование": name_1, "Цена": price_1, "Количетсво": amount_1, "ед": "шт."}
tuple_product1 = (1, dict_product1)
######################################################
name_2 = input("Введите наименование следующего товара: ")
price_2 = input("Введите цену следующего товара: ")
amount_2 = input("Введите кол-во следующего товара: ")

dict_product2 = {"Наименование": name_2, "Цена": price_2, "Количетсво": amount_2, "ед": "шт."}
tuple_product2 = (2, dict_product2)
######################################################
name_3 = input("Введите наименование последнего товара: ")
price_3 = input("Введите цену последнего товара: ")
amount_3 = input("Введите кол-во последнего товара: ")

dict_product3 = {"Наименование": name_3, "Цена": price_3, "Количетсво": amount_3, "ед": "шт."}
tuple_product3 = (3, dict_product3)
######################################################
product_list = [tuple_product1, tuple_product2, tuple_product3]
#  print(product_list)
######################################################
statistic_dict = {
    "Названия товаров": [dict_product1.get("Наименование"), dict_product2.get("Наименование"),
                         dict_product3.get("Наименование")],
    "Цены": [dict_product1.get("Цена"), dict_product2.get("Цена"),
             dict_product3.get("Цена")],
    "Количество товаров": [dict_product1.get("Количетсво"), dict_product2.get("Количетсво"),
                           dict_product3.get("Количетсво")],
    "ед.": [dict_product1.get("ед"), dict_product2.get("ед"),
            dict_product3.get("ед")]
}
print(statistic_dict, sep='\n')


