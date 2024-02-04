from tkinter import *
import window_setter as ws
import show_score

ss = show_score.ShowScore(30, 30, "test")


def splash_screen(frame):
    frame.destroy()
    ss.create_frame()


main_frame = Tk()
main_frame.resizable(False, False)
ws.FullScreenApp(main_frame)
splash_screen(main_frame)

if __name__ == '__main__':
    main_frame.mainloop()

