# Auto-Animal-Restaurant
A script that helps you with the game *Animal Restaurant*.
## Materials

- Android Phone
  - Enter **Developer Mode**
  - Connect the phone with the computer
  - Enter USB Debugging Mode
  - Take `Mi 8` as an example, you need to click the `MIUI version` for seven times to activate the Developer Mode. Besides, you need to turn on the USB Debugging Mode and the secure debugging mode as well.
- python
- pip
- adb
  - [Download from here](https://adb.clockworkmod.com)
  - remember to configure the environment path
  - [Alternative](https://github.com/google/python-adb)

## Intro to Animal Restaurant

- [A brief introduction[CN]](https://www.bilibili.com/read/cv3704392)
- Platform: WeChat APP

## Obtain the coordinates

For android devices, you can use the function *display phone coordinates* in Developer Mode to obtain the coordinates directly.

## Basic operations

- `adb shell` to open adb in cmd

- `getevent -l` to monitor events

- `input tap x y` to simulate clicking (x,y)

- `input swipe x1 y1 x2 y2` to simuate swiping from (x1,y1) to (x2,y2)

- [More](https://www.jianshu.com/p/c58d615700a1)

- [Documentation](https://developer.android.com/studio/command-line/adb)

- call adb

  ```python
  import os
  os.popen(f'{self.hander} {cmd}').read()
  ```

## Optimization

Load the operation from file.

- open `adb shell` in cmd.

- use `getevent -l` to monitor the event. Use the finger to click the target points on the phone, and record the name of the event (*eventX*)

- record the data file to recordtap:

  ```
  adb shell
  dd if=/dev/input/event3 of=/sdcard/recordtap
  ```

  (or similar code)

- then click the target points. After finishing that process, send `Ctrl+C` to cmd.

- read the data file (for testing):

  ```
  adb shell
  dd if=/sdcard/recordtap of=/dev/input/event3
  ```

- loop

  ```
  adb shell
  for i in `seq 1 100`; do dd if=/sdcard/recordtap of=/dev/input/event3;sleep 0.1; done
  ```

  (or similar code)

- sleep

## Credit

[XYstudy](https://github.com/iTimeTraveler/XYStudy) / [code structure 1](https://github.com/colourfate/tap_recorder) / [code structure2](https://github.com/HoPGoldy/easy-animal-restaurant-py) / [opt 1](https://igor.mp/blog/2018/02/23/using-adb-simulate-touch-events.html) / [opt 2](https://zongren.me/2019/03/06/fast-click-android-simulate/#点击屏幕)

