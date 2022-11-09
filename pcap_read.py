from scapy.all import *

packet = rdpcap('1_0.pcapng')
print(packet[0].show())
data = list()
for i in packet:
    if i[ICMP].type==8:
        try:
            if(i[ICMP].load[-2:-1]==b'\x00'):
                data.append('0')
            else:
                data.append('1')
        except:
            pass
print(''.join(data))