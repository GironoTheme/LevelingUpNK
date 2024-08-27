from Tools.vision_controll_package import image


screen = "Images/screenshots/"
temp = "Images/templates/"


class Quests:
    def state(self):
        def accept():
            return image.matching(screen + "accept.png",
                                  temp + "accept.png",
                                  True,
                                  area_of_screenshot=(1753, 121, 1808, 133))

        def complete():
            return image.matching(screen + "complete.png",
                                  temp + "complete.png",
                                  True,
                                  area_of_screenshot=(1744, 121, 1817, 133))

        states = [accept, complete]

        for state in states:
            if state():
                return states.index(state)

        return -1

    def skip(self):
        return image.matching(screen + "skip.png",
                              temp + "skip.png",
                              True,
                              area_of_screenshot=(1757, 51, 1880, 67))


quests = Quests()


# image.take_screenshot(temp+"steed.png", (1620, 121, 1680, 133))