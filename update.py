from scapy.all import conf, sniff
from scan import scan_ip
from tkinter import *
from gui import *


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
    return ip_vars