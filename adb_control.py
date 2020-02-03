import os
import random

class AdbControl:
    hander = 'adb'

    def get_devices(self):
        stdout = self.exec('devices')
        result = []
        for line in stdout.split('\n'):
            if line != 'List of devices attached ' and line:
                result.append(line.split('\t')[0])
        print(result)

    def exec(self, cmd):
        return os.popen(f'{self.hander} {cmd}').read()

    def tap(self, x, y):
        tmp1 = random.randint(0, 15)
        tmp2 = random.randint(0, 15)
        tmp1 = tmp1 - 8
        tmp2 = tmp2 - 8
        x = x + tmp1
        y = y + tmp2
        self.exec(f'shell input tap {x} {y}')

    def fasttap(self):
        tmp = random.randint(85, 105)
        print('Combo is %d' % (tmp))
        self.exec(
            'shell for i in `seq 1 %d`; do dd if=/sdcard/recordtap of=/dev/input/event3;sleep 0.1; done' % (tmp))

    def swipe(self, startX, startY, endX, endY, timeout):
        self.exec(
            f'shell input swipe {startX} {startY} {endX} {endY} {timeout}')
