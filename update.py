from scapy.all import sniff
from scan import scan_ip
from tkinter import *

ip_vars = {}


def load_blocked_ips():
    blocked_ips = set()
    try:
        with open("blocked_ips.txt", "r") as f:
            blocked_ips = set(f.read().splitlines())
    except FileNotFoundError:
        pass
    return blocked_ips


def clear_checkboxes(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, Checkbutton):
            widget.destroy()


def update_ip(frame_good, frame_idk, frame_good_checkbox, frame_idk_checkbox, show_blocked_var):
    global ip_vars
    good_ip, idk_ip = scan_ip()
    blocked_ips = load_blocked_ips()
    clear_checkboxes(frame_good)
    clear_checkboxes(frame_idk)
    if show_blocked_var.get():
        for ip in blocked_ips:
            idk_ip[(ip, None)] = 0 
    add_checkbox(frame_good_checkbox, good_ip)
    add_checkbox(frame_idk_checkbox, idk_ip, blocked_ips)


def add_checkbox(frame, ip_list, blocked_ips=set()):
    i = 1
    for key, value in ip_list.items():
        var = BooleanVar()
        ip_address = key[0]
        is_blocked = ip_address in blocked_ips
        text = f"IP: {ip_address} ({'ЗАБЛОКИРОВАН' if is_blocked else f'{value} запросов'})"
        chk = Checkbutton(frame, text=text, variable=var, fg="#FF0000" if is_blocked else "#F8F8F8", selectcolor="#E75480", bg="#333337")
        chk.grid(row=i, column=0, sticky="w", padx=10, pady=2)
        ip_vars[key] = var
        i += 1

    return ip_vars
