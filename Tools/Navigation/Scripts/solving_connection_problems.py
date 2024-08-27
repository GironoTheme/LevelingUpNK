from time import sleep

from Tools.vision_controll_package import mouse
from Tools.Check.in_main_menu import connection_with_server, ad, afk
from Tools.Navigation.in_main_menu import click_on_start


class SolvingConnectionProblems:
    def solution(self):
        if connection_with_server() or afk():
            self._click_on_ok()
            if not self._remove_ad():
                mouse.click()
            click_on_start()
            sleep(15)

    def _click_on_ok(self):
        mouse.move_and_click(956, 649)
        sleep(2)
        mouse.click()
        sleep(6)

    def _remove_ad(self):
        if ad():
            mouse.move_and_click(1567, 822)
            sleep(0.7)
            mouse.click()
            sleep(6)
            return True
        return False


solving_connection_problems = SolvingConnectionProblems()
solution = solving_connection_problems.solution
