from Tools.vision_controll_package import mouse


class NaSkills:
    def get(self, skill=0):
        mouse.move_and_click(1610, 195 + (95 * skill + 4 * skill))

    def places(self, place):
        start = 657
        formula = start + (75 * place + 8 * place)

        if place > 3:
            place -= 4
            formula = 1013 + (75 * place + 8 * place)
            mouse.move_and_click(formula, 1005)
            mouse.drag(formula, 1022)
            return

        mouse.move_and_click(formula, 1005)
        mouse.drag(formula, 1022)

    def click_on_post_skill(self):
        mouse.move_and_click(1750, 910)


na_skills = NaSkills()



