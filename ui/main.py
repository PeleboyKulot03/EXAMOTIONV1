from tkinter import *
import window_setter as ws


def splash_screen(frame):
    frame.destroy()
    import landing_page


main_frame = Tk()
main_frame.resizable(False, False)
ws.FullScreenApp(main_frame)
splash_screen(main_frame)
main_frame.state('zoomed')


main_frame.mainloop()

