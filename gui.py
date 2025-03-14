#python gui.py
from tkinter import *
from test import scan_ip

#окно
root = Tk() 
root.geometry("900x600")
root.title("idk")
root.configure(bg="#1A1A1D")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0,weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=2)


frame_label = Frame(root, bg="#292A2D")
frame_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
frame_label.grid_columnconfigure(0, weight=1)

frame_good = Frame(root, bg="#292A2D", bd=2, relief="ridge")
frame_good.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
frame_good.grid_rowconfigure(0, weight=0)
frame_good.grid_rowconfigure(1, weight=1)
frame_good.grid_columnconfigure(0, weight=1)
frame_idk = Frame(root, bg="#292A2D", bd=2, relief="ridge")
frame_idk.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")
frame_idk.grid_rowconfigure(0, weight=0)
frame_idk.grid_rowconfigure(1, weight=1)
frame_idk.grid_columnconfigure(0, weight=1)

scroll_good = Scrollbar(frame_good, orient="vertical")
scroll_good.grid(row=1, column=1, sticky="ns")
scroll_idk = Scrollbar(frame_idk, orient="vertical")
scroll_idk.grid(row=1, column=1, sticky="ns")


frame_good_checkbox = Frame(frame_good, bg="#292A2D")
frame_good_checkbox.grid(row=1, column=0, sticky="nsew")
frame_good_checkbox.grid_columnconfigure(0, weight=1)
frame_idk_checkbox = Frame(frame_idk, bg="#292A2D")
frame_idk_checkbox.grid(row=1, column=0, sticky="nsew")
frame_idk_checkbox.grid_columnconfigure(0, weight=1)

Label(frame_label, text="Сканирование сети", fg="#E75480", bg="#292A2D", font=("Arial", 36), anchor="center").grid(row=0, column=0, pady=10, columnspan=3, sticky="nsew")
Label(frame_good, text="Безопасное подключение: ",  fg="#E75480", bg="#292A2D", font=("Arial", 12)).grid(row=0, column=0,sticky="w", pady=10)
Label(frame_idk, text="Подозрительное подключение: ", fg="#E75480", bg="#292A2D", font=("Arial", 12)).grid(row=0, column=0,sticky="w", pady=10)

frame_button = Frame(root, bg="#1A1A1D")
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
    add_checkbox(frame_good_checkbox, good_ip)
    add_checkbox(frame_idk_checkbox, idk_ip)


def add_checkbox(frame, ip_list):
    i=1
    for key, value in ip_list.items():
        var = BooleanVar()
        chk = Checkbutton(frame, text=f"ip: {key} было найдено ({value} запросов)", variable=var, fg="#F8F8F8", selectcolor="#E75480", bg="#333337")
        chk.grid(row=i, column=0, sticky="w", padx=10, pady=2)
        ip_vars[key] = var
        i+=1


btn = Button(frame_button, text="сканировать", font=("Arial", 12, "bold"), bg="#E75480", fg="#F8F8F8", activebackground="#FF85A2", activeforeground="#1A1A1D", relief="raised", padx=10, pady=5, command=lambda: update_ip())
btn.grid(row=0, column=0, sticky="nsew")
#составляющее

root.mainloop()
