# This is created by Edina Berkes and Pál Matolay.
# Py_Game1.4

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
    score = 0
    ground = "'" * 80
    grond_y, ground_x = 6, 0
    title = ' Just Jump! [Beta] ||| Socre: '
    title_x = int((80 - len(title)) / 2)
    ins = "You jump with space, but if you jump too often you won't get score."

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
        win.addstr(0, title_x+30, str(score))
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
                # win.addstr(barriery, barrierx - 30, BARRIER)
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
                # win.addstr(barriery, x, BARRIER)
                win.refresh()
                if barrierx == 0:
                    barrierx = 79
                time.sleep(0.03)
                n = n + 1


# Barrier movement
        barrierx += -1
        win.addstr(barriery, barrierx, BARRIER)
        # win.addstr(barriery, barrierx - 30, BARRIER)
        win.refresh()
        if barrierx == 0:
            barrierx = 79
        time.sleep(0.03)

        if (playerY == 5 and playerX == barrierx):
            # win.addstr(0, 0, "GameOver")
            break

curses.wrapper(main)
