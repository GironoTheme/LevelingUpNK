from Tools.vision_controll_package import image

screen = "Images/screenshots/"
temp = "Images/templates/"


def connection_with_server():
    return image.matching(screen+"connection_with_server.png",
                          temp+"connection_with_server.png",
                          True,
                          area_of_screenshot=(692, 378, 1228, 704))


def afk():
    return image.matching(screen + "afk.png",
                          temp + "afk.png",
                          True,
                          area_of_screenshot=(691, 375, 1231, 706))


def ad():
    return image.matching(screen+"ad.png",
                          temp+"ad.png",
                          True,
                          area_of_screenshot=(1548, 804, 1583, 839))
