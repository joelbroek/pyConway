import curses
import time
import numpy as np
import random



def main():
    """Initialises Conway's Game of Life
    """
    DURATION = 50

    screen = curses.initscr()
    yx = screen.getmaxyx()
    HEIGHT = yx[1] - 1
    WIDTH = yx[0] - 1
    curses.noecho()
    curses.curs_set(0)
    iteration = 0
    panel = get_new_panel(HEIGHT, WIDTH, isRandom = True)

    def draw_panel():
        for y in range(0, HEIGHT):
            for x in range (0, WIDTH):
                if panel[y][x] == 1:
                    screen.addstr(x,y,"X")
                else:
                    screen.addstr(x,y," ")
        screen.refresh()

    draw_panel()
    
    while iteration < DURATION:
        time.sleep(1)
        iteration += 1
        prev_panel = panel
        panel = get_next_panel(prev_panel, HEIGHT, WIDTH)
        draw_panel()

    curses.endwin()

def get_new_panel(h, w, isRandom):
    """Generates a h * w ndarray for Conway's game. If isRandom, filled randomly from [0,1] else 0

    Args:
        h (int): height of panel
        w (int): width of panel
        isRandom (bool): whether panel should be filled randomly from [0,1], or with 0

    Returns:
        ndarray: the new panel
    """
    panel = np.ndarray((h,w), dtype = np.int32)
    for y in range(0,h):
        for x in range(0,w):
            panel[y][x] = random.randint(0,1) if isRandom else 0
    return panel


def get_next_panel(prev_panel, h, w):
    """Generates next panel for Conway's Game of Life

    Args:
        prev_panel (ndarray): [array with dimension h * w]
        h (int): height of panel
        w (int): width of panel

    Returns:
        ndarray: next panel of Conway's Game
    """
    panel = get_new_panel(h, w, False) # get blank scene


    # gather adjacency data
    for y in range(0, h):
        for x in range(0, w):
            if x - 1 >= 0: # LEFT
                panel[y][x] += prev_panel[y][x-1]
                if y + 1 < h: # LEFT & DOWN
                    panel[y][x] += prev_panel[y+1][x-1]
                if y - 1 >= 0: # LEFT & UP
                    panel[y][x] += prev_panel[y-1][x-1]
            if x + 1 < w: # RIGHT
                panel[y][x] += prev_panel[y][x+1]
                if y + 1 < h: # RIGHT & DOWN
                    panel[y][x] += prev_panel[y+1][x+1]
                if y - 1 >= 0: # RIGHT & UP
                    panel[y][x] += prev_panel[y-1][x+1]
            if y - 1 >= 0: panel[y][x] += prev_panel[y-1][x] # UP
            if y + 1 < h: panel[y][x] += prev_panel[y+1][x] # DOWN

    new_panel = get_new_panel(h,w,False)

    # determines which cells should be alive in next iteration
    for y in range(0,h):
        for x in range(0,w):
            if prev_panel[y][x] == 0 and panel[y][x] == 3:
                new_panel[y][x] = 1
            elif prev_panel[y][x] == 1 and panel[y][x] <=3 and panel[y][x] >= 2:
                new_panel[y][x] = 1
                
    return new_panel

if __name__ == "__main__":
        main()
