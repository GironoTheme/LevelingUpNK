from time import sleep

from Tools.vision_controll_package.MouseAndKeyboard.mouse_actions import mouse


class NaInventory:
    def sorting_through_items(self, func, gain=False):
        x_cords = (1497, 1574)
        y_cords = (150, 226)
        if gain is True:
            x_cords = (1482, 1557)
            y_cords = (137, 213)

        width = x_cords[1] - x_cords[0]
        height = y_cords[1] - y_cords[0]
        horizontal_distance = 7
        vertical_distance = 6

        x_start_first = x_cords[0]
        y_start_first = y_cords[0]

        rows = 6
        columns = 4

        for row in range(rows):
            for col in range(columns):
                x_start = x_start_first + col * (width + horizontal_distance)
                y_start = y_start_first + row * (height + vertical_distance)
                x_center = x_start + width / 2
                y_center = y_start + height / 2

                mouse.move_and_click(x_center, y_center)
                if func() == 1:
                    return
                print([x_start, y_start])

    def all(self):
        mouse.move_and_click(1887, 185)

    def armor(self):
        mouse.move_and_click(1887, 270)

    def close(self):
        mouse.move_and_click(1880, 105)

    def chest(self):
        mouse.move_and_click(1880, 370)

    def auto(self):
        mouse.move_and_click(1880, 470)

    def click_on_max_button(self):
        mouse.move_and_click(1140, 665)

    def click_on_ok_in_sweet_menu(self):
        mouse.move_and_click(1080, 780)
        sleep(0.7)
        mouse.click()

    def take_sweet(self, sweet):
        mouse.move_and_click(785 + (80 * sweet + 7 * sweet), 400)

    def click_on_auto_use(self):
        mouse.move_and_click(1390, 593)


na_inventory = NaInventory()
