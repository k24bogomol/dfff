#cd C:\Users\User\Documents\GitHub\dfff
#python test.py

from scapy.all import conf, IP, TCP, sniff

ip_count = {}
good_ip = {}
idk_ip = {}

def packet_check(packet):
    if IP in packet and TCP in packet:
       key = (packet[IP].src, packet[TCP].dport)
       ip_count[key] = ip_count.get(key, 0) + 1

def scan_ip():
    sniff(iface="enp0s3", count = 10, prn = packet_check)
    for key, value in ip_count.items():
        if value >= 3:
            idk_ip[key] = value
        else:
            good_ip[key] = value

    print("Безопасные соединения:")
    for key, value in good_ip.items():
        print(f"IP: {key[0]}, порт: {key[1]} - {value} запросов")

    print("Подозрительные соединения:")
    for key, value in idk_ip.items():
        print(f"По IP {key[0]} на порт {key[1]} обнаружено {value} запросов")

    return good_ip, idk_ip


       

#def packet_info(packet):
#    print("пойман пакет: " + packet.summary())
#sniff(iface="Intel(R) Wi-Fi 6 AX201 160MHz", count = 10, prn = packet_info)

#def packet_check(packet):
#    if (f"{packet[IP].src}") in ip_count:
#       ip_count[(f"{packet[IP].src}")] = (count+=1)
#    else:
#        count = 0
#        ip_count[(f"{packet[IP].src}")] = count
