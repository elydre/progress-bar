'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
 - codé en : UTF-8
 - langage : python 3
 - GitHub  : github.com/pf4-DEV
 - Licence : GNU GPL v3
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

import os

version = "0.0.2"

class Bar:
    def __init__(self, nb, char="=", display_mode="p"):
        """
        nb: number of steps
        char: char to display
        display_mode: "p" percents, "s" steps, "n" nothing
        """
        
        self.longueur = os.get_terminal_size().columns - 3
        self.nb = nb
        self.char = char
        self.steps = [round(x * (self.longueur / self.nb)) for x in range(self.nb + 1)]
        self.display_mode = display_mode

        print("progress bar initialized")

    def go_up(self):
        print(end="\033[F")
        print(end="\033[K")

    def get_display(self, step): # you can change this function to display custom things
        if self.display_mode == "p": return f" {round(step / self.nb * 100)}% "
        if self.display_mode == "s": return f" {step}/{self.nb} "
        return ""

    def progress(self, step):
        
        to_display = self.get_display(step)
        display_zone = list(range(round(self.longueur / 2 - len(to_display) / 2), round(self.longueur / 2 + len(to_display) / 2)))

        self.go_up()
        print(end="[")

        for i in range(self.longueur):
            if i in display_zone:
                print(end = to_display)
                to_display = ""

            elif i < self.steps[step]:
                print(self.char, end="")
            else:
                print(" ", end="")

        print("]")