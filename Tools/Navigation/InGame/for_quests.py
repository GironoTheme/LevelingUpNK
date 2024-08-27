from time import sleep

from Tools.vision_controll_package import mouse


class ForQuests:
    def click_on_quest(self, twice=False):
        mouse.move_and_click(1780, 125)
        if twice:
            sleep(0.8)
            mouse.click()

    def click_on_skip(self):
        mouse.move_and_click(1813, 59)

    def click_on_ok(self):
        mouse.move_and_click(1060, 740)


for_quests = ForQuests()



