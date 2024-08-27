from Tools.vision_controll_package import image


screen = "Images/screenshots/"
temp = "Images/templates/"


def check_category():
    return image.matching(screen + "category_is_visible.png",
                          temp + "category_is_visible.png",
                          True,
                          area_of_screenshot=(34, 92, 66, 127))


# image.take_screenshot(temp+"steed.png", (1620, 121, 1680, 133))