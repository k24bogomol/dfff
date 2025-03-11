from scapy.all import conf, IP, TCP, sniff

print("Начинаем перехват пакетов...")
sniff(count=10, prn=print)
print("Перехват окончен!")
