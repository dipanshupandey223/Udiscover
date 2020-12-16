import scapy.all as scapy
from optparse import OptionParser


parser = OptionParser()
parser.add_option("--ip", dest="ipadress", help="Enter the IP or Range")
(keys, values) = parser.parse_args()
target = str(keys.ipadress)
def scan(ip):
    arp_request = scapy.ARP(pdst=target)
    ethernet_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    new_packet_combined = ethernet_packet/arp_request
    answered_list = scapy.srp(new_packet_combined, timeout=1, verbose=False)[0]
    print("IP\t\t\t Mac")
    print("-"*50)
    for element in answered_list:
        print(element[1].psrc, '\t\t', element[1].hwsrc)

scan(target)