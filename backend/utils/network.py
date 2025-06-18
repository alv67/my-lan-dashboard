from scapy.layers.l2 import ARP, Ether, srp
import ipaddress
import requests
from datetime import datetime

def scan_network(ip_range):
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for sent, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "hostname": get_hostname(received.psrc),
            "vendor": get_vendor_from_mac(received.hwsrc),
            "last_seen": datetime.now().isoformat()
        })

    return devices

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Nome host sconosciuto"

def get_vendor_from_mac(mac_address):
    try:
        response = requests.get(f'https://api.macvendors.com/{mac_address}', timeout=2)
        if response.status_code == 200:
            return response.text
        return "Vendor sconosciuto"
    except:
        return "Vendor sconosciuto"