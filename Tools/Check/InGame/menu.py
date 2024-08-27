from Tools.vision_controll_package import image


screen = "Images/screenshots/"
temp = "Images/templates/"


def close_right_menus():
    return image.matching(screen + "close_right_menus.png",
                          temp + "close_right_menus.png",
                          True,
                          area_of_screenshot=(1865, 88, 1897, 121))

    # image.take_screenshot(temp + "close_right_menus.png", (1865, 88, 1897, 121))


def grave():
    return image.matching(screen + "grave.png",
                          temp + "grave.png",
                          True,
                          area_of_screenshot=(1504, 20, 1512, 66))
    # image.take_screenshot(temp + "grave.png", (1504, 20, 1512, 66))

