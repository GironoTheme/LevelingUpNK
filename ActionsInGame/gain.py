from time import sleep

from Tools.Check.InGame.ch_gain import equipped_in_gain, register_materials
from Tools.Check.InGame.ch_inventory import ch_inventory
from Tools.Navigation.InGame import main_buttons
from Tools.Navigation.InGame.na_inventory import na_inventory
from Tools.vision_controll_package.MouseAndKeyboard.mouse_actions import mouse


def accept_gains():
    def gain():
        if equipped_in_gain():
            if register_materials():
                mouse.move_and_click(1535, 1000)
            if not register_materials() and not ch_inventory.may_collapse():
                mouse.move_and_click(325, 990)
                sleep(1.2)

    na_inventory.sorting_through_items(gain, gain=True)
    main_buttons.quit_big_menu()





