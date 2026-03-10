from scapy.all import sniff, IP, TCP, UDP, ICMP
from database import insert_packet


def process_packet(packet):

    if IP in packet:

        src = packet[IP].src
        dst = packet[IP].dst
        length = len(packet)

        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"

        elif UDP in packet:
            protocol = "UDP"

        elif ICMP in packet:
            protocol = "ICMP"

        insert_packet(src, dst, protocol, length)

        print(f"{src} -> {dst} | {protocol} | {length}")


def start_sniffer():

    sniff(prn=process_packet, store=False)
