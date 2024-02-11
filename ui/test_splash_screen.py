from tkinter import *
import window_setter as ws


main_frame = Tk()
main_frame.resizable(False, False)
main_frame.config(bg='#2B2D42')
ws.FullScreenApp(main_frame)
main_frame.state('zoomed')


main_frame.mainloop()
