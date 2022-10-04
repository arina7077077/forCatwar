import pyautogui
import random
from pynput.keyboard import *

#  ======== settings ========
delay = random.randint(120, 140)  # in seconds
resume_key = Key.f2
pause_key = Key.enter
exit_key = Key.esc
x_key = Key.tab
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Начали]")
    elif key == pause_key:
        pause = True
        print("[Пауза]")
    elif key == exit_key:
        running = False
        print("[Выход]")
    elif key == x_key:
        x = pyautogui.position()
        print(x)



def display_controls():

    print("\t Время первого клика = " + str(delay) + ' секунд' + '\n')
    print("// - Инструкция:")
    print("\t Запусти код, зайди на локацию, наведись на первый переход, нажми tab, вернись в консоль, посмотри координаты")
    print("\t Впиши их в 56 строку")
    print("\t tab = Узнай координаты второго перехода")
    print("\t Впиши их в 59 строку")
    print("\t F2 = Запусть кликер")
    print("\t enter = Остановить кликер")
    print("-----------------------------------------------------")
    print('Нажмите F2 для старта')

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.moveTo(511, 347)
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            pyautogui.moveTo(899, 992)
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay

    lis.stop()

if __name__ == "__main__":
    main()
