from classes import Store, Shop, Request

if __name__ == '__main__':
    shop = Shop()
    store = Store()

    store.add('печеньки', 3)
    store.add('собачки', 3)
    store.add('коробки', 5)
    store.add('елки', 20)

    shop.add('собачки', 2)
    shop.add('коробки', 5)

    print("\nВ склад хранится:")
    for i in store.get_items():
        print(store.get_items()[i], i)
    print("\nВ магазин хранится:")
    for i in shop.get_items():
        print(shop.get_items()[i], i)

    request = Request(input('Введите запрос: '))
    if request.fromm == 'склад' and request.product in store.get_items() and store.get_items()[request.product] >= request.amount:
        print('Нужное количество есть на складе')
        store.remove(request.product, request.amount)
        print(f'Курьер везет {request.amount} {request.product} со склад в магазин')
        shop.add(request.product, request.amount)
        print("\nВ склад хранится:")
        for i in store.get_items():
            print(store.get_items()[i], i)
        print("\nВ магазин хранится:")
        for i in shop.get_items():
            print(shop.get_items()[i], i)

        # if request.product in store.get_items() and store.get_items()[request.product] >= request.amount:
        #     print(f'Нужное количество "{request.product}" есть на складе')
        #     store.remove(request.product, request.amount)
        #     print(f'Курьер везет {request.amount} {request.product} со склад в магазин')
        #     shop.add(request.product, request.amount)
        #     print("\nВ склад хранится:")
        #     for i in store.get_items():
        #         print(store.get_items()[i], i)
        #     print("\nВ магазин хранится:")
        #     for i in shop.get_items():
        #         print(shop.get_items()[i], i)
    else:
        print(f'"{request.product}" Не хватает на складе, попробуйте заказать меньше')
