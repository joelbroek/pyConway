import curses
import time
import threading
import numpy as np
import random



def main():
    """Initialises Conway's Game of Life
    """
    # Constants
    HEIGHT = 12
    WIDTH = 12
    DURATION = 4

    screen = curses.initscr()
    curses.noecho()

    curses.curs_set(0)
    iteration = 0
    panel = get_scene(HEIGHT, WIDTH, isRandom = True)

    def draw_panel():
        for y in range(0, HEIGHT):
            for x in range (0, WIDTH):
                if panel[y][x] == 1:
                    screen.addstr(y,x,"X")
                else:
                    screen.addstr(y,x," ")
        screen.refresh()

    draw_panel()
    
    while iteration < DURATION:
        time.sleep(1)
        iteration += 1
        screen.addstr(0, WIDTH + 5, str(iteration))
        prev_panel = panel
        panel = get_next_panel(prev_panel, HEIGHT, WIDTH)
        screen.refresh()
        # TODO

    curses.endwin()

def get_scene(h, w, isRandom):
    panel = np.ndarray((h,w), dtype = np.int32)
    for y in range(0,h):
        for x in range(0,w):
            panel[y][x] = random.randint(0,1) if isRandom else 0
    return panel


def get_next_panel(prev_panel, h, w):
    panel = get_scene(h, w, False) # get blank scene

if __name__ == "__main__":
        main()
