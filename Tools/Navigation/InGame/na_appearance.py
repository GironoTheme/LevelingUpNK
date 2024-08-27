from Tools.Check.InGame.ch_appearance import ch_accept_appearance
from Tools.vision_controll_package import mouse


def appearance_categories(func):
    for category in range(9):
        mouse.move_and_click(1873, 275 + (64 * category))
        if func():
            break


def accept_appearance():
    if ch_accept_appearance():
        mouse.move_and_click(1710, 1035)
        return True

