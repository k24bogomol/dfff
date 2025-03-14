#python gui.py
from tkinter import *
from test import scan_ip

#окно
root = Tk() 
root.geometry("900x600")
root.title("idk")
root.configure(bg="#DBC5D1")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0,weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=2)


frame_label = Frame(root, bg="#DBC5D1")
frame_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
frame_label.grid_columnconfigure(0, weight=1)

frame_good = Frame(root, bg="#C38DAE")
frame_good.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
frame_idk = Frame(root, bg="red")
frame_idk.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")

Label(frame_label, text="Сканирование сети", bg="#C38DAE", font=("Arial", 36), anchor="center").grid(row=0, column=0, pady=10, columnspan=3, sticky="nsew")
Label(frame_good, text="Безопасное подключение: ",  bg="#C38DAE", font=("Arial", 12)).grid(row=0, column=0, pady=10)
Label(frame_idk, text="Подозрительное подключение: ", bg="#C38DAE", font=("Arial", 12)).grid(row=0, column=1, pady=10)

frame_button = Frame(root, bg="#dbc5d1")
frame_button.grid(row=2, column=1, padx=30, pady=30, sticky="nsew")
#окно

#составляющее
ip_vars = {}

def clear_checkboxes(frame):
    for widget in frame.winfo_children():  
        if isinstance(widget, Checkbutton):  
            widget.destroy() 

def update_ip ():
    good_ip, idk_ip = scan_ip()
    clear_checkboxes(frame_good)
    clear_checkboxes(frame_idk)
    add_checkbox(frame_good, good_ip)
    add_checkbox(frame_idk, idk_ip)


def add_checkbox(frame, ip_list):
    i=0
    for key, value in ip_list.items():
        var = BooleanVar()
        chk = Checkbutton(frame, text=f"ip: {key} было найдено ({value} запросов)", variable=var, bg=frame["bg"])
        chk.grid(row=i, column=0, sticky="w", padx=10)
        ip_vars[key] = var
        i+=1


btn = Button(frame_button, text="сканировать", command=lambda: update_ip())
btn.grid(row=0, column=0, sticky="nsew")
#составляющее

root.mainloop()
