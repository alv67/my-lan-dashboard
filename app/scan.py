from scapy.all import ARP, Ether, srp
import socket
import uuid
import netifaces
import ipaddress

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connessione fittizia per ottenere l'IP locale
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_local_mac():
    mac = uuid.getnode()
    return ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(40, -1, -8)])

def get_all_local_ips_and_macs():
    devices = []
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs and netifaces.AF_LINK in addrs:
            ip = addrs[netifaces.AF_INET][0]['addr']
            mac = addrs[netifaces.AF_LINK][0]['addr']
            # Escludi loopback e interfacce senza MAC valido
            if ip != "127.0.0.1" and mac and mac != "00:00:00:00:00:00":
                devices.append({"ip": ip, "mac": mac})
    return devices

def scan_network(ip_range):
    # Crea un pacchetto ARP su Ethernet
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    # Invia il pacchetto e riceve le risposte
    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for sent, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    # Aggiungi solo gli IP/MAC locali che appartengono al range
    local_devices = get_all_local_ips_and_macs()
    net = ipaddress.ip_network(ip_range, strict=False)
    for local in local_devices:
        if (ipaddress.ip_address(local["ip"]) in net) and not any(d["ip"] == local["ip"] for d in devices):
            devices.append(local)

    return devices

# Esempio: sostituisci con il range della tua rete, es: 192.168.1.0/24
devices = scan_network("192.168.1.0/24")

for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")