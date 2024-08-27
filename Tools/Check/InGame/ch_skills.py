from time import sleep
from Tools.vision_controll_package import image


screen = "Images/screenshots/"
temp = "Images/templates/"


def skill_equipped():
    sleep(0.4)
    return image.matching(screen + "skill_equipped.png",
                          temp + "skill_equipped.png",
                          True,
                          area_of_screenshot=(1108, 159, 1127, 178))


