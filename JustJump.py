# This is created by Edina Berkes and Pál Matolay.
# Py_Game1.6

import curses
import time
import random


def speed_setting(barrierx, s):
    speed = 0.03
    if barrierx == 0:
        barrierx = 79
    # elif s > 100 and s < 300:
    #     speed = 0.02
    # elif s > 300:
    #     speed = 0.01
    time.sleep(speed)
    return barrierx, s


def main(scr):
    curses.LINES = 10
    curses.noecho()
    curses.curs_set(0)
    win = curses.newwin(10, 80, 0, 0)
    win.keypad(1)
    win.border(0)
    win.nodelay(1)
    win.refresh()

    BARRIER = "█"
    barriery, barrierx = 5, 79
    PLAYER = "©"
    playerY, playerX = 5, 5
    score = 0
    ground = "░" * 80
    grond_y, ground_x = 6, 0
    title = ' - - - - Just Jump! 2000© [2.0] ||| Score:     - - - - -'
    title_x = int((80 - len(title)) / 2)
    ins = """ You jump with space, but if you jump too often you won't get score.
 If you can't dodge the barrier you lost!
 PRESS [ q ] TO QUIT."""

    while True:
        if True:
            score += 1
        win.refresh()
        win.clear()
        # Player movement(display, move)
        win.addstr(playerY, playerX, PLAYER)
        win.refresh()
        event = win.getch()
        win.addstr(0, title_x, title)
        win.addstr(0, title_x + 43, str(score))
        win.addstr(grond_y, ground_x, ground)
        win.addstr(7, 0, ins)
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
                barrierx, score = speed_setting(barrierx, score)
                n = n + 1

            # Fall
            while n > 3 and n < 10:
                win.addstr(playerY, playerX, " ")
                playerY += 1
                win.getch()
                win.addstr(barriery, barrierx, " ")
                win.addstr(playerY, playerX, PLAYER)
                barrierx += -1
                win.addstr(barriery, barrierx, BARRIER)
                win.refresh()
                barrierx, score = speed_setting(barrierx, score)
                n = n + 1


# Barrier movement
        barrierx += -1
        win.addstr(barriery, barrierx, BARRIER)
        win.refresh()
        barrierx, score = speed_setting(barrierx, score)

        if (playerY == 5 and playerX == barrierx):
            break

curses.wrapper(main)
