from adb_control import AdbControl
import random
import time
import json


class RestaurantControl:

    def __init__(self):
        self.adb = AdbControl()

    def my_order(self):
        for i in range(0, 3):
            tmp = random.randint(1, 5)
            if tmp == 1:
                self.my_service()
            elif tmp == 2:
                self.my_collection()
            elif tmp == 3:
                self.my_call()
            elif tmp == 4:
                self.my_call()
            elif tmp == 5:
                self.my_call()
            self.my_delay()
        self.my_service()
        self.my_delay()
        print(f'Current loop end.\n')
        return True

    def my_delay(self):
        tmp = random.randint(2, 800) * 0.001
        print('The delay is: %f\n' % (tmp))
        time.sleep(tmp)
        return True

    def my_call(self):
        print(f'Start calling people:')
        # for i in range(0,28):
        #     self.adb.tap(955,2020)
        self.adb.fasttap()
        return True

    def my_service(self):
        print(f'Start ordering:')
        self.adb.tap(400, 800)
        self.adb.tap(680, 810)
        self.adb.tap(930, 820)
        self.adb.tap(409, 1168)
        self.adb.tap(663, 1172)
        self.adb.tap(926, 1177)
        return True

    def my_collection(self):
        print(f'Start collecting money:')
        self.adb.tap(130, 889)
        self.adb.tap(440, 972)
        self.adb.tap(700, 970)
        self.adb.tap(981, 990)
        self.adb.tap(441, 1334)
        self.adb.tap(687, 1329)
        self.adb.tap(966, 1316)
        self.adb.tap(443, 1645)
        self.adb.tap(475, 1823)
