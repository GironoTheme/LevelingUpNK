from time import sleep

from ActionsInGame.in_inventory import in_inventory
from Tools.Navigation.InGame import main_buttons
from Tools.Navigation.InGame.na_outpost import na_output
from Tools.vision_controll_package import mouse


class Purchase:
    def go_to_outpost(self):
        in_inventory.click_on_teleport()

    def something_in_something_category(self, category, func):
        na_output.click_on_category(category)
        sleep(1)
        func()
        na_output.click_on_back()

    def purchase_of_consumables(self):
        def consumables():
            self.buy_treatment()
            self.buy_assault_drug()
            self.buy_victory_potion()
            self.buy_teleports()

        self.go_to_outpost()
        self.something_in_something_category(0, consumables)

    def buy_treatment(self):
        mouse.move_and_click(210, 160)
        na_output.buy_hundred_pieces(3)

    def buy_assault_drug(self):
        mouse.move_and_click(200, 510)
        na_output.buy_ten_pieces()

    def buy_victory_potion(self):
        mouse.move_and_click(200, 615)
        na_output.buy_by_piece(6)

    def buy_teleports(self):
        mouse.move_and_click(220, 855)
        na_output.buy_by_piece(1)

    def buy_skills(self):
        na_output.click_on_category(4)
        mouse.move_and_click(185, 335)
        na_output.click_on_buy()
        sleep(3.5)

        mouse.move_and_click(205, 910)
        na_output.click_on_buy()
        sleep(3.5)
        main_buttons.quit_big_menu()


purchase = Purchase()

