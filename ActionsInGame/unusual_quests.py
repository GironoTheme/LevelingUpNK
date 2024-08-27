from time import sleep
from ActionsInGame.in_inventory import in_inventory
from ActionsInGame.purchase import purchase
from ActionsInGame.skills import skills
from Tools.Check.InGame.ch_appearance import ch_accept_appearance
from Tools.Check.InGame.ch_rebirth import check_rebirth
from Tools.Check.InGame.quests import quests
from Tools.Navigation.InGame.main_buttons import quit_big_menu, click_on_rebirth
from Tools.Navigation.InGame.na_appearance import appearance_categories, accept_appearance
from Tools.Navigation.InGame.steeds import accept, quit_steeds
from Tools.Navigation.InGame.for_quests import for_quests
from Tools.Navigation.Scripts.solving_connection_problems import solution
from Tools.logger import logger
from Tools.vision_controll_package.MouseAndKeyboard.mouse_actions import mouse
from counter import increment_counter


class UnusualQuests:
    def steed(self):
        for_quests.click_on_quest()
        sleep(0.7)
        accept()
        quit_steeds()
        sleep(0.7)
        for_quests.click_on_quest()

    def glaider(self):
        def skip_text():
            if quests.skip():
                while quests.skip():
                    for_quests.click_on_skip()
                    sleep(1.5)
                return 0

        def execute_with_skip(func, *args, **kwargs):
            func(*args, **kwargs)
            skip_text()

        execute_with_skip(for_quests.click_on_quest)
        sleep(0.7)
        execute_with_skip(accept)
        sleep(0.7)
        execute_with_skip(accept)
        execute_with_skip(quit_steeds)
        sleep(0.7)
        execute_with_skip(for_quests.click_on_quest)

        sleep(35)
        execute_with_skip(for_quests.click_on_ok)

    def apply_appearance_of_weapon(self):
        for_quests.click_on_quest()
        appearance_categories(accept_appearance)
        quit_big_menu()
        for_quests.click_on_quest()

        while quests.state() != 1:
            sleep(3)

    def promotion(self):
        for_quests.click_on_quest()
        mouse.move_and_click(185, 240)
        mouse.move_and_click(160, 1030)
        sleep(1)
        mouse.move_and_click(1060, 650)
        sleep(1)
        quit_big_menu()
        for_quests.click_on_quest()
        sleep(20)

    def buy_cool_skills(self):
        def default_quests():
            def _new_quest(twice=False):
                for_quests.click_on_quest(twice)
                increment_counter()

            def _exception_handling():
                if quests.skip():
                    while quests.skip():
                        for_quests.click_on_skip()
                        sleep(1.5)
                    return 0

                if solution():
                    return 0

                if check_rebirth():
                    click_on_rebirth()
                    sleep(3.5)
                    in_inventory.dress_up()
                    in_inventory.collecting_sweets()
                    in_inventory.auto_potions()
                    purchase.purchase_of_consumables()
                    for_quests.click_on_quest()

                sleep(2.3)
                return 1
            state_of_quest = quests.state()
            match state_of_quest:
                case 0:
                    for_quests.click_on_quest()
                case 1:
                    _new_quest(True)
                    return True
                case -1:
                    _exception_handling()

            return False

        in_inventory.click_on_teleport()
        purchase.buy_skills()
        in_inventory.learn_skills()
        skills.install_skills()
        for_quests.click_on_quest()

        while not default_quests():
            sleep(3)


unusual_quests = UnusualQuests()

