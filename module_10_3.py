from threading import Thread, Lock
from random import randint
import time

lock = Lock()

class Bank:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            with lock:
                rand_num = randint(50, 500)
                self.balance = self.balance + rand_num
                print(f'Пополнение: {rand_num}. Баланс {self.balance}')
                # if self.balance >= 500 and lock.locked():
                #     lock.release()
            time.sleep(0.001)

    def take(self):
        for k in range(100):
            with lock:
                rand_num = randint(50, 500)
                print(f'Запрос на {rand_num}')
                if rand_num <= self.balance:
                    self.balance = self.balance - rand_num
                    print(f'Снятие: {rand_num}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, не достаточно средств')
                    # lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
