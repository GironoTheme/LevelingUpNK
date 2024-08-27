from ActionsInGame.completing_quests import completing_quests
from ActionsInGame.in_inventory import in_inventory
from ActionsInGame.purchase import purchase
from Tools.Check.InGame.ch_gain import equipped_in_gain, register_materials
from Tools.Check.InGame.ch_inventory import ch_inventory
from Tools.Check.InGame.menu import close_right_menus, grave
from Tools.Navigation.in_main_menu import click_on_start
from Tools.Navigation.Scripts.solving_connection_problems import solution
from Tools.Check.in_main_menu import connection_with_server, ad, afk
from Tools.Check.InGame.quests import quests
from Tools.vision_controll_package.Windows.windows import Windows
from counter import write_counter

windows = Windows()


def test(hwnd):
    completing_quests.manipulations_with_quests()


def start():
    windows.switch_windows(test)


def edit_counter(count):
    write_counter(count)

#edit_counter()
start()







# quests.state()
    #print(ad())
    # afk()
    # solution()
# ch_inventory.equipped([1498, 150])
    # quests.steed()
    # inventory.gloves()
    # close_right_menus()