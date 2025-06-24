import time
from pydirectinput import *
import pydirectinput
import random
import ctypes
import rich
from rich import print
from tkinter import messagebox

NULLBRIGHT1 = " ███▄    █  █    ██  ██▓     ██▓     ▄▄▄▄    ██▀███   ██▓  ▄████  ██░ ██ ▄▄▄█████▓"
NULLBRIGHT2 = " ██ ▀█   █  ██  ▓██▒▓██▒    ▓██▒    ▓█████▄ ▓██ ▒ ██▒▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒"
NULLBRIGHT3 = "▓██  ▀█ ██▒▓██  ▒██░▒██░    ▒██░    ▒██▒ ▄██▓██ ░▄█ ▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░"
NULLBRIGHT4 = "▓██▒  ▐▌██▒▓▓█  ░██░▒██░    ▒██░    ▒██░█▀  ▒██▀▀█▄  ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ "
NULLBRIGHT5 = "▒██░   ▓██░▒▒█████▓ ░██████▒░██████▒░▓█  ▀█▓░██▓ ▒██▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ "
NULLBRIGHT6 = "░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░░▒▓███▀▒░ ▒▓ ░▒▓░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   "
NULLBRIGHT7 = "░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░ ▒  ░░ ░ ▒  ░▒░▒   ░   ░▒ ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    "
NULLBRIGHT8 = "   ░   ░ ░  ░░░ ░ ░   ░ ░     ░ ░    ░    ░   ░░   ░  ▒ ░░ ░   ░  ░  ░░ ░  ░      "
NULLBRIGHT9 = "         ░    ░         ░  ░    ░  ░ ░         ░      ░        ░  ░  ░  ░         "
NULLBRIGHT10 = "                                          ░                                       "

hi = "Hi from NULLBRIGHT v4!"

NULLBRIGHTq = "NULLBRIGHT v4 : "

menu = """
/##################################################################################################/
/                                           NULLBright v4                                          /
/                                               MENU                                               /
----------------------------------------------------------------------------------------------------
/ AutoFarm   (arbuz/carrot/beet/wheat)                                             (Working...)    /
/ FarmLava   (count/timer)                                                         (Coming soon...)/
/ FarmStone  (count/timer)                                                         (Coming soon...)/
/ FarmDirt   (wall/post/cube/block)                                                (Coming soon...)/
/ AutoStor   (shalker/chest) (X;Y of chest) (slots)                                (Coming soon...)/
/ AutoEat    (cake/food) (timer/custom)                                            (Coming soon...)/
/ AutoClicker(mouse/keyboard) (interval) (SecBeforeStart) (count) (key/button)     (Working...)    /
/ AutoTool   (tool/timer/end farm)                                                 (Coming soon...)/
/ AutoSell   (command) (64/timer/custom)                                           (???)           /
/ AutoLeave  (command/leave) (end farm/timer)                                      (???)           /
"""

print(f"[bold #570057]{NULLBRIGHT1}[/bold #570057]")
print(f"[bold #6e006e]{NULLBRIGHT2}[/bold #6e006e]")
print(f"[bold #800080]{NULLBRIGHT3}[/bold #800080]")
print(f"[bold #8c008c]{NULLBRIGHT4}[/bold #8c008c]")
print(f"[bold #9b009b]{NULLBRIGHT5}[/bold #9b009b]")
print(f"[bold #a800a8]{NULLBRIGHT6}[/bold #a800a8]")
print(f"[bold #b700b7]{NULLBRIGHT7}[/bold #b700b7]")
print(f"[bold #c100c1]{NULLBRIGHT8}[/bold #c100c1]")
print(f"[bold #cd00cd]{NULLBRIGHT9}[/bold #cd00cd]")
print(f"[bold #d900d9]{NULLBRIGHT10}[/bold #d900d9]")
print(f"[bold green]{hi}[/bold green]")

def move_mouse_sneaky(dx, dy, duration=1.0):
    steps = 50
    for _ in range(steps):
        x = dx // steps + random.randint(-2, 2)
        y = dy // steps + random.randint(-2, 2)
        ctypes.windll.user32.mouse_event(0x0001, x, y, 0, 0)
        time.sleep(duration / steps)

Hi2 = "NULLBRIGHT, this is a bot of minecraft for AutoFarm, AutoLava, AutoStone, AutoDirt, AutoChest, AutoHunger, AutoAh, AutoLeave, AutoTool, and more functions...!"

print(f"[bold #cd4bcd]{menu}[/bold #cd4bcd]")
print(f"[bold #9b009b]{Hi2}[/bold #9b009b]")

Function = input("Function : ")
