from abc import abstractmethod


class Storage:
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for i in self.items.keys():
                if name == i:
                    self.items[i] += count
                    is_found = True
                    print(f'Курьер доставил {count} {name}')
            if not is_found:
                self.items[name] = count
                print(f'Новый товар "{name}" добавлен')
        else:
            print(f'Товар в количестве {count}шт. не может быть добавлен, т.к. есть место только для '
                  f'{self.get_free_space()}шт.')

    def remove(self, name, count):
        if name in self.items.keys():
            if self.items[name] >= count:
                self.items[name] -= count
                print(f'Курьер забрал {count} {name} со склада')
            else:
                print(f'{name} Не хватает на складе, попробуйте заказать меньше')
        else:
            print(f'{name} отсутствует на складе')

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.capacity = 20
        self.limit = limit

    @property
    def get_item_limit(self):
        return self.limit

    def add(self, name, count):
        if self.get_unique_items_count() < self.limit:
            super().add(name, count)
        else:
            print(f'Товар не может быть добавлен')


class Request:
    def __init__(self, strr: str):
        lst = self.get_info(strr)
        self.fromm = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    def get_info(self, strr: str):
        return strr.split(' ')

    def __repr__(self):
        return f'Доставить** {self.amount} {self.product} **из** {self.fromm} **в** {self.to}'
