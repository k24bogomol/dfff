from scapy.all import conf, sniff
active_ip = conf.route.route("0.0.0.0")[0]
print(active_ip)


#python mistakes.py
#cd C:\Users\User\Documents\GitHub\dfff