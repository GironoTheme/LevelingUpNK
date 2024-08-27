from time import sleep

from Tools.Check.InGame.ch_outpost import check_category
from Tools.vision_controll_package import mouse


class NaOutpost:
    def click_on_category(self, category):
        mouse.move_and_click(115, 107 + (47 * category + 2 * category))

        while check_category():
            sleep(2.5)

    def click_on_back(self):
        mouse.move_and_click(44, 40)

    def buy_ten_pieces(self, dozen=1):
        for i in range(0, dozen):
            mouse.move_and_click(915, 665)
        self.click_on_buy()

    def buy_by_piece(self, dozen=1):
        for i in range(0, dozen):
            mouse.move_and_click(1100, 450)
        self.click_on_buy()

    def buy_hundred_pieces(self, dozen=1):
        for i in range(0, dozen):
            mouse.move_and_click(1005, 665)
        self.click_on_buy()

    def click_on_buy(self):
        mouse.move_and_click(1060, 875)
        sleep(1)


na_output = NaOutpost()

