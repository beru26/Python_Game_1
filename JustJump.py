# This is created by Edina Berkes and Pál Matolay.
# Py_Game1.3

import curses
import time
import random


def main(scr):
    curses.LINES = 10
    curses.noecho()
    curses.curs_set(0)
    win = curses.newwin(10, 80, 0, 0)
    win.keypad(1)
    win.border(0)
    win.nodelay(1)
    win.refresh()

    BARRIER = "Ψ"
    barriery, barrierx = 5, 79
    PLAYER = "•"
    playerY, playerX = 5, 5

    while True:
        win.clear()
        # Player movement(display, move)
        win.addstr(playerY, playerX, PLAYER)
        win.refresh()
        event = win.getch()
        title = ' Just Jump! [Beta] '
        win.addstr(0, (curses.COLS - len(title)) // 2, title)
        if event == ord("q"):
            break
        elif event == ord(" "):
            n = 0
            # Jump up
            while n < 5:
                win.addstr(playerY, playerX, " ")
                playerY += -1
                win.addstr(playerY, playerX, PLAYER)
                win.getch()
                win.addstr(barriery, barrierx, " ")
                barrierx += -1
                win.addstr(barriery, barrierx, BARRIER)
                win.refresh()
                if barrierx == 0:
                    barrierx = 79
                time.sleep(0.03)
                n = n + 1

            # Fall
            while n > 4 and n < 10:
                win.addstr(playerY, playerX, " ")
                playerY += 1
                win.addstr(playerY, playerX, PLAYER)
                win.getch()
                win.addstr(barriery, barrierx, " ")
                barrierx += -1
                win.addstr(barriery, barrierx, BARRIER)
                win.refresh()
                if barrierx == 0:
                    barrierx = 79
                time.sleep(0.03)
                n = n + 1


# Barrier movement
        barrierx += -1
        win.addstr(barriery, barrierx, BARRIER)
        win.refresh()
        if barrierx == 0:
            barrierx = 79
        time.sleep(0.03)
        if (playerY == 5 and playerX == barrierx):
            break

curses.wrapper(main)
