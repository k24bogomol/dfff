from scapy.all import conf, IP, sniff

ip_count = {}

#def packet_check(packet):
#    if (f"{packet[IP].src}") in ip_count:
#       ip_count[(f"{packet[IP].src}")] = (count+=1)
#    else:
#        count = 0
#        ip_count[(f"{packet[IP].src}")] = count

def packet_check(packet):
    if IP in ip_count:
       ip_count[(f"{packet[IP].src}")] = (count+=1)
    else:
        count = 0
        ip_count[(f"{packet[IP].src}")] = count


print(conf.ifaces + "\n")
sniff(count = 10, prn = packet_check)
for key, value in ip_count.items:
    print(f"по данному айпи ({key}) обнаружено: ({value}) запросов")

       

#def packet_info(packet):
#    print("пойман пакет: " + packet.summary())
#sniff(iface="Intel(R) Wi-Fi 6 AX201 160MHz", count = 10, prn = packet_info)