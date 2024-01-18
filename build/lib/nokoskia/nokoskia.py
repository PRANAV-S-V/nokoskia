import curses 
from curses import wrapper
import time

def get_terminal_size(stdscr):
    # Get terminal size
    height, width = stdscr.getmaxyx()
    return height, width

def init_custom_colors():
    # Define custom color pairs
    # Yellow foreground, black background
    curses.init_color(100, 1000, 894, 345)  # Define custom color #F8E559 as yellow
    curses.init_pair(1, 100, curses.COLOR_BLACK)  # Yellow foreground, black background

    # White foreground, blue background
    curses.init_color(101, 76, 725, 913)  # Define custom color #4CB9E7 as blue
    curses.init_pair(2, curses.COLOR_WHITE, 101)  # White foreground, blue background
    curses.init_pair(3, 101, 100)  # Blue foreground, Yellow background
    curses.init_pair(4, 100, 101)  # Yellow foreground, blue background



def knock():
    def main(stdscr):
        # Check if the terminal supports colors
        curses.start_color()
        init_custom_colors()
        curses.curs_set(0)
            
        stdscr.clear()
        stdscr.refresh()

        # Adding the co-ordinates to be the top-left corner as default.
        x = 0
        y = 0
        start = True
        # Splitting the dialogue into two variables making it easy to change the color of the sentences in the same line.
        part1 = "I am the One Who "
        part2 = "KNOCKS."

        # Making the loop always true to give it an infinite behavior.
        try:
            while start:
                # Getting the size of the terminal window to avoid errors like "characters out of the visible area error."
                height, width = get_terminal_size(stdscr)
                center_x = int(height / 2)
                center_y = int(width / 2)
                width = width - len(part1 + part2)
                # Checking whether the line is within the visible area.
                if x < height and y < width:
                    stdscr.addstr(x, y, part1, curses.color_pair(1))
                    stdscr.addstr(x, y + len(part1), part2, curses.color_pair(2) | curses.A_BOLD)
                    x = x + 1
                    second = len(part1 + part2)
                    stdscr.refresh()
                # If the line is going to be outside the visible area:
                elif y < width:
                    # Erase the screen and start from the beginning.
                    stdscr.erase()
                    x = 0
                    y = (y + second)  # Loop horizontally=second
                else:
                    # presenting an end-credit before the program stops.
                    start = False
                    stdscr.erase()
                    stdscr.addstr(center_x, center_y, "NoW sAy ", curses.color_pair(3) | curses.A_BOLD)
                    stdscr.addstr(center_x, center_y+len("NoW sAy "), "My NaMe", curses.color_pair(4) | curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(2)
                time.sleep(0.06)
        # handling the keyboard Interrupt by user.
        except KeyboardInterrupt:
            pass
        finally:
            curses.endwin() 
            

    wrapper(main)



