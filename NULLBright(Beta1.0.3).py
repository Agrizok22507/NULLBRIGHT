from tkinter import messagebox
import time
import ctypes
import random
import rich
from rich import print
import pydirectinput

def move_mouse_sneaky(dx, dy, duration=1.0):
    steps = 50
    for _ in range(steps):
        x = dx // steps + random.randint(-2, 2)
        y = dy // steps + random.randint(-2, 2)
        ctypes.windll.user32.mouse_event(0x0001, x, y, 0, 0)
        time.sleep(duration / steps)

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

hi = "Hi from NULLBRIGHT!"
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

Activate = input("Do you want Active(y/n) : ")
BlockX = int(input("(blocks, x;y y=9)x : "))
def gotostart():
    pydirectinput.keyUp('w')
    time.sleep(BlockX)
    pydirectinput.keyDown('w')
    pydirectinput.keyUp('a')
    time.sleep(BlockX)
    pydirectinput.keyDown('a')

def spam_sobrat():
    while not STOP_SOBRAT:
        pydirectinput.doubleClick()
        time.sleep(0.1)
stop_norm_sobrat = False
STOP_SOBRAT = False
def sobrat():
    while not stop_norm_sobrat:
        print("sobrat...")
        pydirectinput.keyUp('d')
        time.sleep(BlockX)
        pydirectinput.keyUp('s')
        time.sleep(0.6)
        pydirectinput.keyDown('s')
        pydirectinput.keyUp('a')
        time.sleep(BlockX)
        pydirectinput.keyUp('a')
        pydirectinput.mouseDown(button='left')

def posev():
    print("posev...")
    pydirectinput.mouseUp(button='right')
    pydirectinput.keyUp('d')
    time.sleep(BlockX)
    pydirectinput.keyUp('s')
    time.sleep(0.6)
    pydirectinput.keyDown('s')
    pydirectinput.keyUp('a')
    time.sleep(BlockX)
    pydirectinput.keyUp('a')
    pydirectinput.mouseDown(button='right')


def main():
    active = "Activating..."
    print(f"[bold green]{active}[/bold green]")
    AutoEat = input("AutoEat(y/n) : ")
    AutoAh = input("AutoAh(y/n) : ")
    time.sleep(5)
    move_mouse_sneaky(0, 1500)
    farm()
def farm():
    gotostart()
    spam_sobrat()
    sobrat()
    sobrat()
    sobrat()
    sobrat()
    sobrat()
    sobrat()
    sobrat()
    sobrat()
    sobrat()
    STOP_SOBRAT = True
    stop_norm_sobrat = True
    gotostart()
    posev()
    posev()
    posev()
    posev()
    posev()
    posev()
    posev()
    posev()
    posev()
    gotostart()
    time.sleep(800)
    STOP_SOBRAT = False
    stop_norm_sobrat = False
    farm()

if Activate == "y":
    main()
else:
    ok = "Ok"
    print(f"[bold green]{ok}[/bold green]")
# python NULLBright(Beta1.0.3).py
