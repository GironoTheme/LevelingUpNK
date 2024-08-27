from Tools.Check.InGame.ch_skills import skill_equipped
from Tools.Navigation.InGame.na_skills import na_skills
from Tools.Navigation.InGame.main_buttons import click_on_skills, close_right_hand_menus


class Skills:
    def install_skills(self):
        click_on_skills()
        places = 0
        na_skills.click_on_post_skill()

        for i in range(6):
            na_skills.get(i)
            if skill_equipped():
                places += 1
                continue

            na_skills.places(places)
            places += 1

        close_right_hand_menus()


skills = Skills()


