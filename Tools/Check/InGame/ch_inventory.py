from Tools.vision_controll_package import image
from time import sleep

screen = "Images/screenshots/"
temp = "Images/templates/"


class ChInventory:
    def outerwear(self):
        return image.matching(screen + "outerwear.png",
                              temp + "outerwear.png",
                              True,
                              area_of_screenshot=(1150, 305, 1193, 318))

    def shoes(self):
        return image.matching(screen + "shoes.png",
                              temp + "shoes.png",
                              True,
                              area_of_screenshot=(1150, 305, 1193, 318))

    def helmet(self):
        return image.matching(screen + "helmet.png",
                              temp + "helmet.png",
                              True,
                              area_of_screenshot=(1150, 304, 1190, 318))

        # image.take_screenshot(temp + "helmet.png", (1150, 304, 1190, 318))

    def gloves(self):
        return image.matching(screen + "gloves.png",
                              temp + "gloves.png",
                              True,
                              area_of_screenshot=(1150, 304, 1216, 318))
        #image.take_screenshot(temp + "gloves.png", (1150, 304, 1216, 318))

    def equipped(self):
        sleep(0.4)
        return image.matching(screen + "equipped.png",
                              temp + "equipped.png",
                              True,
                              area_of_screenshot=(1111, 152, 1130, 170))
        # image.take_screenshot(temp + "equipped.png", (1111, 152, 1130, 170))
    def teleport(self):
        return image.matching(screen + "teleport.png",
                              temp + "teleport.png",
                              True,
                              area_of_screenshot=(1153, 279, 1254, 288))
        # image.take_screenshot(temp + "teleport.png", (1153, 279, 1254, 288))

    def max_button(self):
        sleep(0.3)
        return image.matching(screen + "max_button.png",
                              temp + "max_button.png",
                              True,
                              area_of_screenshot=(1100, 650, 1180, 687))

    def scroll_in_chest(self):
        return image.matching(screen + "scroll_in_chest.png",
                              temp + "scroll_in_chest.png",
                              True,
                              area_of_screenshot=(760, 370, 810, 430))
        # image.take_screenshot(temp + "scroll_in_chest.png", (760, 370, 810, 430))

    def gain_scroll(self):
        sleep(0.3)
        return image.matching(screen + "gain_scroll.png",
                              temp + "gain_scroll.png",
                              True,
                              area_of_screenshot=(1150, 278, 1200, 289))
        # image.take_screenshot(temp + "gain_scroll.png", (1150, 278, 1200, 289))

    def auto_use(self):
        sleep(0.3)
        return image.matching(screen + "auto_use.png",
                              temp + "auto_use.png",
                              True,
                              area_of_screenshot=(1368, 581, 1422, 603))
        # image.take_screenshot(temp + "auto_use.png", (1368, 581, 1422, 603))

    def chest_of_items(self):
        sleep(0.3)
        return image.matching(screen + "chest_of_items.png",
                              temp + "chest_of_items.png",
                              True,
                              area_of_screenshot=(1151, 278, 1180, 288))
        # image.take_screenshot(temp + "chest_of_items.png", (1151, 278, 1180, 288))

    def food_basket(self):
        sleep(0.3)
        return image.matching(screen + "food_basket.png",
                              temp + "food_basket.png",
                              True,
                              area_of_screenshot=(1119, 185, 1178, 218))

    def may_collapse(self):
        sleep(0.3)
        return image.matching(screen + "may_collapse.png",
                              temp + "may_collapse.png",
                              True,
                              area_of_screenshot=(342, 928, 432, 937))
        # image.take_screenshot(temp + "may_collapse.png", (342, 928, 432, 937))
ch_inventory = ChInventory()





    # image.take_screenshot(temp+"steed.png", (1150, 305, 1193, 318))