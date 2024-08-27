from time import sleep

from Tools.vision_controll_package import mouse


def click_on_inventory():
    mouse.move_and_click(1723, 40)


def click_on_auto():
    mouse.move_and_click(1868, 768)


def click_on_skills():
    mouse.move_and_click(1796, 43)


def close_right_hand_menus():
    mouse.move_and_click(1880, 105)
    sleep(0.6)


def quit_big_menu():
    mouse.move_and_click(1874, 42)


def click_on_rebirth():
    mouse.move_and_click(1790, 1030)



