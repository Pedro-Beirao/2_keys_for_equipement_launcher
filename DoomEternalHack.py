#!/usr/bin/python3

from pynput import mouse,keyboard
from pynput.mouse import Controller, Button
import time
import threading

keyboardd = keyboard.Controller()

throwEquipementKey = "o"
switchEquipementKey = "p"


isIce = False
isGrenade = True

bindTimes=2

print("Press the key to throw a Grenade:")

def on_press(key):
    global grenadeKey
    global iceKey

    global bindTimes

    global isGrenade
    global isIce

    if bindTimes==2:
        grenadeKey=key
        bindTimes=1
        print('Grenade key set to: {0}'.format(key))
        time.sleep(1)
        print("\nPress the key to throw a Ice Bomb:")

    elif bindTimes==1:
        iceKey=key
        bindTimes=0
        print('Ice Bomb key set to: {0}'.format(key))
        time.sleep(1)
        print("\nYou are all set.\n\n!!Rip and Tear!!")
        print("\n(If you close this window, the program will stop)")


    elif isIce:
        if key == grenadeKey:
            isGrenade=True
            isIce=False
            keyboardd.press(switchEquipementKey)
            time.sleep(0.1)
            keyboardd.press(throwEquipementKey)
            print("ice bomb")
        elif key == iceKey:
            keyboardd.press(throwEquipementKey)
            print("grenade")

    elif isGrenade:
        if key == iceKey:
            isGrenade=False
            isIce=True
            keyboardd.press(switchEquipementKey)
            time.sleep(0.1)
            keyboardd.press(throwEquipementKey)
            print("bomb")
        elif key == grenadeKey:
            keyboardd.press(throwEquipementKey)
            print("bomb")






listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
