from threading import Thread
import time
from queue import Queue
import random


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(1, 2))
        print(f'{self.name} покушал(-а) и ушёл(ушла)')


class Cafe(Queue):
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            self.queue.put(guest)
            print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    table.guest.join()
                    if not table.guest.is_alive():
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None


tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()





