from time import sleep
from ActionsInGame.in_inventory import in_inventory
from ActionsInGame.purchase import purchase
from ActionsInGame.unusual_quests import unusual_quests
from ActionsInGame.skills import skills
from Tools.Check.InGame.ch_rebirth import check_rebirth
from Tools.Navigation.InGame.main_buttons import click_on_rebirth
from Tools.Navigation.Scripts.restoration_of_lost import restoration
from Tools.Navigation.in_main_menu import click_on_start
from Tools.Check.InGame.quests import quests
from Tools.Navigation.InGame.for_quests import for_quests
from Tools.Navigation.Scripts.solving_connection_problems import solution
from Tools.logger import logger
from counter import read_counter, increment_counter


class CompletingQuests:
    def __init__(self):
        self.special_quests = {
            1: click_on_start,
            7: unusual_quests.steed,
            10: unusual_quests.glaider,
            16: in_inventory.dress_up,
            18: skills.install_skills,
            23: unusual_quests.apply_appearance_of_weapon,
            43: unusual_quests.promotion,
            52: unusual_quests.buy_cool_skills

        }

    def manipulations_with_quests(self):
        while True:
            try:
                counter = read_counter()
                print(counter)

                if counter in self.special_quests:
                    self._exception_handling()
                    self.special_quests[counter]()
                    self.default_quests()
                else:
                    self.default_quests()

                sleep(6.5)
            except KeyboardInterrupt:
                break

            except Exception as e:
                logger.error(f"Произошла ошибка: {e}")
                break

    def default_quests(self):
        state_of_quest = quests.state()
        match state_of_quest:
            case 0:
                for_quests.click_on_quest()
            case 1:
                self._new_quest(True)
                return True
            case -1:
                self._exception_handling()

        return False

    def _new_quest(self, twice=False):
        for_quests.click_on_quest(twice)
        increment_counter()

    def _exception_handling(self):
        if quests.skip():
            while quests.skip():
                for_quests.click_on_skip()
                sleep(1.3)
            return 0

        if solution():
            return 0

        if check_rebirth():
            click_on_rebirth()
            sleep(6)
            restoration()
            in_inventory.dress_up()
            in_inventory.collecting_sweets()
            in_inventory.auto_potions()
            purchase.purchase_of_consumables()
            for_quests.click_on_quest()

        sleep(1.8)
        logger.warning("Никакое из состояний не было найдено")
        return 1


completing_quests = CompletingQuests()




