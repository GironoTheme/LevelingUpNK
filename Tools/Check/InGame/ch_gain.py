from Tools.vision_controll_package import image
from time import sleep

screen = "Images/screenshots/"
temp = "Images/templates/"


def equipped_in_gain():
    sleep(0.35)
    return image.matching(screen + "equipped_in_gain.png",
                          temp + "equipped_in_gain.png",
                          True,
                          area_of_screenshot=(161, 240, 177, 256))


def register_materials():
    sleep(0.35)
    return image.matching(screen + "register_materials.png",
                          temp + "register_materials.png",
                          True,
                          area_of_screenshot=(225, 673, 348, 685))
    # image.take_screenshot(temp + "register_materials.png", (225, 673, 348, 685))