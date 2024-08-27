from time import sleep
from Tools.vision_controll_package import image


screen = "Images/screenshots/"
temp = "Images/templates/"


def check_rebirth():
    sleep(0.4)
    return image.matching(screen + "rebirth.png",
                          temp + "rebirth.png",
                          True,
                          area_of_screenshot=(1680, 1005, 1885, 1053))
    # image.take_screenshot(temp + "rebirth.png", (1680, 1005, 1885, 1053))

