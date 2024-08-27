from Tools.Check.InGame.menu import grave
from Tools.vision_controll_package.MouseAndKeyboard.mouse_actions import mouse


def restoration():
    if grave():
        click_on_grave()
        iterating_through_restorations()
        close_grave_menu()


def click_on_grave():
    mouse.move_and_click(1508, 38)


def iterating_through_restorations():
    for i in range(1):
        mouse.move_and_click(40, 180 + (100 * i))
        repair()


def repair():
    mouse.move_and_click(250, 910)


def close_grave_menu():
    mouse.move_and_click(40, 105)



