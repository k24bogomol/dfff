#python gui.py
from tkinter import *
from test import scan_ip

#окно
root = Tk()
root.geometry("300x300")
root.title("idk")
root.configure(bg="#DBC5D1")

frame_good = Frame(root, bg="#C38DAE")
frame_good.pack(padx=10, pady=10)
#окно

#составляющее
btn = Button(root, text="сканировать", command=lambda: scan_ip())
btn.pack()
#

root.mainloop()
