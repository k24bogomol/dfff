from update import ip_vars
import os

BLOCKED_IPS_FILE = "blocked_ips.txt"

def load_blocked_ips():
    if os.path.exists(BLOCKED_IPS_FILE):
        with open(BLOCKED_IPS_FILE, "r") as f:
            return set(f.read().splitlines())
    return set()

def save_blocked_ips(blocked_ips):
    with open(BLOCKED_IPS_FILE, "w") as f:
        f.write("\n".join(blocked_ips))

def ban_ip():
    blocked_ips = load_blocked_ips()
    for key in ip_vars:
        if isinstance(key, tuple) and ip_vars[key].get():
            IP = key[0]
            if IP not in blocked_ips:   
                os.system(f"sudo iptables -A INPUT -s {IP} -j DROP")
                blocked_ips.add(IP)
                print(f"IP {IP} заблокирован :)")
    save_blocked_ips(blocked_ips)

    


def unban_ip():
    blocked_ips = load_blocked_ips()
    for key in ip_vars:
        if isinstance(key, tuple) and ip_vars[key].get():
            IP = key[0]
            if IP in blocked_ips:   
                os.system(f"sudo iptables -D INPUT -s {IP} -j DROP")
                blocked_ips.remove(IP)
                print(f"IP {IP} разблокирован :)")
    save_blocked_ips(blocked_ips)
