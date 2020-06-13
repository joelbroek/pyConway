import curses
import time
import threading

# Constants
HEIGHT = 12
WIDTH = 12
DURATION = 24

def main():
    """Initialises Conway's Game of Life
    """

    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    iteration = 0

    while iteration < DURATION:
        time.sleep(1)
        ++iteration

    curses.endwin()

if __name__ == "__main__":
        main()
