from update import ip_vars
import os

def ban_ip (ip_vars):
    blocked_ips = set()
    for key in ip_vars:
        if isinstance(key, tuple) and  getattr(ip_vars[key], "get", lambda: False)():
            IP = key[0]
            if IP not in blocked_ips:   
                os.system(f"sudo iptables -A INPUT -s {IP} -j DROP")
                blocked_ips.add(IP)
                print(f"айпи {IP} заблокирован :)")
