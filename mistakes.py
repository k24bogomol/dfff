from scapy.all import conf, sniff
print("Начинаем перехват пакетов...")
sniff(iface="Intel(R) Wi-Fi 6 AX201 160MHz", count=1, prn=print)
print("Перехват окончен!")


#python mistakes.py
#cd C:\Users\User\Documents\GitHub\dfff