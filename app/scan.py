"""
# scan.py
# Uno script Python per la scansione di rete che rileva gli indirizzi IP e MAC dei dispositivi connessi.
# Richiede i permessi di root per funzionare correttamente.
# Utilizza le librerie scapy e netifaces per l'interazione con la rete.
# Assicurati di eseguire questo script con i permessi di amministratore.
# Esempio di utilizzo:
sudo python3 scan.py
"""

import socket
import uuid
import os
import sys
import ipaddress
import requests
from dns import resolver, reversename
import json
from datetime import datetime

from scapy.layers.l2 import ARP, Ether, srp
import netifaces

def get_local_ip():
    """Ottiene l'indirizzo IP locale della macchina."""
    # Crea un socket UDP per ottenere l'IP locale
    # Utilizza un socket UDP per evitare di dover connettersi a un server remoto
    # Questo metodo è più affidabile per ottenere l'IP locale rispetto a sock
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connessione fittizia per ottenere l'IP locale
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_local_mac():
    """Ottiene l'indirizzo MAC locale della macchina."""
    mac = uuid.getnode()
    return ':'.join(['{:02x}'.format((mac >> ele) & 0xff) for ele in range(40, -1, -8)])

def get_all_local_ips_and_macs():
    """Ottiene tutti gli indirizzi IP e MAC delle interfacce di rete locali."""
    devices = []
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs and netifaces.AF_LINK in addrs:
            ip = addrs[netifaces.AF_INET][0]['addr']
            mac = addrs[netifaces.AF_LINK][0]['addr']
            # Escludi loopback e interfacce senza MAC valido
            if ip != "127.0.0.1" and mac and mac != "00:00:00:00:00:00":
                devices.append({
                    "ip": ip, 
                    "mac": mac,
                    "hostname": "Dispositivo locale",
                    "vendor": get_vendor_from_mac(mac),
                    "last_seen": datetime.now().isoformat()
                })
    return devices

def check_root():
    """Verifica se lo script è eseguito come root"""
    if os.geteuid() != 0:
        print("Errore: Questo script deve essere eseguito come root/amministratore.")
        print("Usa: sudo python3 scan.py")
        sys.exit(1)

def get_vendor_from_mac(mac_address):
    """Ottiene il vendor da un MAC address usando l'API di macvendors.com"""
    try:
        # Formatta il MAC address
        #mac = mac_address.replace(':', '').upper()
        mac = mac_address
        response = requests.get(f'https://api.macvendors.com/{mac}', timeout=2)
        if response.status_code == 200:
            return response.text
        return "Vendor sconosciuto"
    except:
        return "Vendor sconosciuto"

def get_hostname(ip):
    """Prova a risolvere il nome host da un IP"""
    try:
        addr = reversename.from_address(ip)
        return str(resolver.resolve(addr, "PTR")[0])
    except:
        return "Nome host sconosciuto"

def scan_network(ip_range):
    """
    Scansiona la rete per trovare dispositivi attivi nel range specificato.
    Args:
        ip_range (str): Il range di IP da scansionare, ad esempio "192.168.1.0/24"
    Returns:
        list: Una lista di dizionari contenenti gli indirizzi IP e MAC dei dispositivi trovati.
    """
    try:
        # Crea un pacchetto ARP su Ethernet
        arp_request = ARP(pdst=ip_range)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast / arp_request

        # Invia il pacchetto e riceve le risposte
        answered, _ = srp(packet, timeout=2, verbose=False)

        devices = []
        for sent, received in answered:
            hostname = get_hostname(received.psrc)
            vendor = get_vendor_from_mac(received.hwsrc)
            devices.append({
                "ip": received.psrc,
                "mac": received.hwsrc,
                "hostname": hostname,
                "vendor": vendor,
                "last_seen": datetime.now().isoformat()
            })

        # Aggiungi solo gli IP/MAC locali che appartengono al range
        local_devices = get_all_local_ips_and_macs()
        net = ipaddress.ip_network(ip_range, strict=False)
        for local in local_devices:
            if (ipaddress.ip_address(local["ip"]) in net) and not any(d["ip"] == local["ip"] for d in devices):
                devices.append(local)

        return devices
    except PermissionError:
        print("Errore: Permessi insufficienti per eseguire la scansione di rete.")
        print("Usa: sudo python3 scan.py")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica i permessi root all'avvio
    check_root()
    
    # Esempio: sostituisci con il range della tua rete, es: 192.168.1.0/24
    try:
        devices = scan_network("192.168.1.0/24")
        for device in devices:
            print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}, Vendor: {device['vendor']}, Last Seen: {device['last_seen']}")
    except (OSError, ValueError) as e:
        print(f"Si è verificato un errore: {str(e)}")
        sys.exit(1)