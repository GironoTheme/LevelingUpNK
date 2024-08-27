from time import sleep

from ActionsInGame.gain import accept_gains
from Tools.Check.InGame.ch_inventory import ch_inventory
from Tools.Check.InGame.ch_outpost import check_category
from Tools.Navigation.InGame import main_buttons
from Tools.Navigation.InGame.main_buttons import click_on_inventory
from Tools.Navigation.InGame.na_inventory import na_inventory
from Tools.vision_controll_package import mouse
from random import randint


class InInventory:
    def collecting_sweets(self):
        def check_sweet():
            if not ch_inventory.teleport():
                self.baskets_and_chests_of_items()
                if ch_inventory.gain_scroll():
                    mouse.click()
                    accept_gains()
                if ch_inventory.max_button():
                    na_inventory.click_on_max_button()
                    if ch_inventory.scroll_in_chest():
                        take_and_confirm_sweet(randint(0, 2))

        def take_and_confirm_sweet(sweet_index):
            na_inventory.take_sweet(sweet_index)
            na_inventory.click_on_ok_in_sweet_menu()
            sleep(0.6)

        click_on_inventory()
        na_inventory.chest()
        na_inventory.sorting_through_items(check_sweet)
        main_buttons.close_right_hand_menus()

    def auto_potions(self):
        def ap():
            if ch_inventory.auto_use():
                na_inventory.click_on_auto_use()
        click_on_inventory()
        na_inventory.auto()
        na_inventory.sorting_through_items(ap)
        main_buttons.close_right_hand_menus()

    def dress_up(self):
        def up():
            sleep(0.7)
            if not ch_inventory.equipped():
                print(ch_inventory.equipped())
                mouse.click()

        click_on_inventory()
        na_inventory.armor()
        na_inventory.sorting_through_items(up)
        na_inventory.close()

    def learn_skills(self):
        def learn():
            sleep(0.6)
            if not ch_inventory.teleport():
                print(ch_inventory.teleport())
                mouse.click()

        for i in range(3):
            click_on_inventory()
            na_inventory.chest()
            na_inventory.sorting_through_items(learn)

            na_inventory.close()

    def click_on_teleport(self):
        def tel():
            sleep(0.6)
            if ch_inventory.teleport():
                print(ch_inventory.teleport())
                mouse.click()
                return 1
        click_on_inventory()
        na_inventory.chest()
        na_inventory.sorting_through_items(tel)

        while not check_category():
            sleep(2.5)

        sleep(1)
        na_inventory.close()

    def baskets_and_chests_of_items(self):
        if ch_inventory.food_basket():
            mouse.click()
            na_inventory.click_on_max_button()
            na_inventory.take_sweet(1)
            na_inventory.click_on_ok_in_sweet_menu()

        if ch_inventory.chest_of_items():
            mouse.click()
            na_inventory.click_on_max_button()
            na_inventory.take_sweet(4)
            na_inventory.click_on_ok_in_sweet_menu()


in_inventory = InInventory()

