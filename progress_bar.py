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
from ColorPrint import colorprint

version = "0.0.4"

class Bar:
    def __init__(self, step, char="=", display_mode="p", longueur = 0):
        """
        nb: number of steps
        char: char to display
        display_mode: "p" percents, "s" steps, "c" clean
        """
        
        self.longueur = longueur or os.get_terminal_size().columns - 3
        self.nb = step
        self.char = char
        self.steps = [round(x * (self.longueur / self.nb)) for x in range(self.nb + 1)]
        self.gradient = [(255, i, 0) for i in range(100, 255)] + [(255 - i, 255, 0) for i in range(255)] + [(0, 255, i) for i in range(255)]
        self.display_mode = display_mode
        print("progress bar initialized")

    def go_up(self):
        print(end="\033[F")
        print(end="\033[K")

    def get_display(self, step): # you can change this function to display custom things
        if "p" in self.display_mode: return f" {round(step / self.nb * 100)}% "
        if "s" in self.display_mode: return f" {step}/{self.nb} "
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
                colorprint(self.char, self.gradient[round(len(self.gradient) * (i / self.longueur))], "k")

            else:
                print(" ", end="")

        print("]")