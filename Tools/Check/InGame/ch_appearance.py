from time import sleep

from Tools.vision_controll_package import image


screen = "Images/screenshots/"
temp = "Images/templates/"


def ch_accept_appearance():
    sleep(0.4)
    image.take_screenshot(screen+"accept_appearance.png", (1650, 1025, 1660, 1040))
    mc_accept = image.get_main_color(screen + "accept_appearance.png")
    if mc_accept[0] >= 200 and mc_accept[1] >= 190 and mc_accept[2] >= 180:
        return True
    return False


    # return image.matching(screen + "accept_appearance.png",
    #                       temp + "accept_appearance.png",
    #                       True,
    #                       area_of_screenshot=(1590, 1010, 1820, 1060))


