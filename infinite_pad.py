#!/usr/bin/python

import curses


class InfinitePad():

    def __init__(self, screen, height, width, y_start, x_start):
        self.screen = screen
        self.height = height
        self.width = width
        self.y_start = y_start
        self.x_start = x_start

        self.pad_top = 0
        self.pad_pos = 0

        self.pad = curses.newpad(self.height * 3, self.width)

    def write(self, message):
        for line in message.split('\n'):
            if self.pad_pos < self.height:
                self.pad.addnstr(self.pad_pos, 0, line, self.width)
            else:
                # We write the string twice, one to the current vie
                # and once to the top of the bad for when we reset.
                pad_b = self.pad_pos - self.height
                self.pad.addnstr(self.pad_pos, 0, line, self.width)
                self.pad.addnstr(pad_b, 0, line, self.width)

            # We should probably do this only when we have written everything
            self.pad.refresh(self.pad_top, 0,
                             self.y_start, self.x_start,
                             self.y_start + self.height - 1, self.x_start + self.width)

            if self.pad_pos == (self.height * 2) - 1:
                # Reset
                self.pad_top = 1
                self.pad_pos = self.height
            elif self.pad_pos >= self.height - 1:
                self.pad_pos = self.pad_pos + 1
                self.pad_top = (self.pad_pos - self.height) + 1
            else:
                self.pad_top = 0
                self.pad_pos = self.pad_pos + 1


if __name__ == "__main__":
    import time
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(1)

    log_pad = InfinitePad(screen, 5, 100, 8, 8)

    for y in range(0, 60):
        log_pad.write("%s: %s" % (y, time.strftime("%a, %d %b %Y %H:%M:%S +0000")))
        time.sleep(3)

    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
