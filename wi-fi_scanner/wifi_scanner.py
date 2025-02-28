import os
import subprocess

def banner():
    print("\n\n----------------------")
    print("    WELCOME TO LUNISECX")
    print("   Wifi Scanner Tool")
    print("----------------------\n")

def check_monitor_mode():
    # Wi-Fi adaptörünün monitor modda olup olmadığını kontrol eder.
    command = "iw dev"
    result = subprocess.getoutput(command)
    
    if "type monitor" in result:
        return True
    else:
        return False

def switch_to_monitor_mode():
    # Wi-Fi adaptörünü monitor moda alır.
    print("Monitor moda geçiş yapılıyor...")
    interface = "wlan0"  # Wi-Fi adaptörünün adı, gerekiyorsa değiştirebilirsiniz
    command = f"sudo ip link set {interface} down"
    subprocess.run(command, shell=True)
    command = f"sudo iw dev {interface} set type monitor"
    subprocess.run(command, shell=True)
    command = f"sudo ip link set {interface} up"
    subprocess.run(command, shell=True)
    print(f"{interface} artık monitor modda.")

def scan_wifi():
    print("Tarama başlatılıyor... Lütfen bekleyin.")
    command = "sudo airodump-ng wlan0"
    
    try:
        # airodump-ng komutunu terminalde çalıştırıyoruz ve çıktıyı ekrana yazdırıyoruz
        subprocess.run(command, shell=True, check=True)
    except KeyboardInterrupt:
        print("\nTarama kesildi. Kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        print("Wi-Fi ağlarını tararken bir sorun meydana geldi.")

def scan_single_network(target_bssid):
    print(f"Belirtilen ağın detayları taranıyor: {target_bssid}")
    command = f"sudo airodump-ng --bssid {target_bssid} wlan0"
    
    try:
        # Tek bir ağın detaylarını tarıyoruz
        subprocess.run(command, shell=True, check=True)
    except KeyboardInterrupt:
        print("\nTarama kesildi. Kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        print(f"Ağı tararken bir sorun meydana geldi: {target_bssid}")

def help_command():
    print("""
Kullanabileceğiniz komutlar:

1. scan_wifi    : Wi-Fi ağlarını tarar.
2. scan_single  : Belirli bir ağın detaylarını tarar (BSSID kullanarak).
3. help         : Yardım menüsünü görüntüler.
4. exit         : Programdan çıkış yapar.

'scan_wifi' komutunu kullanarak, Wi-Fi ağlarını tarayabilir ve ağ bilgilerini görebilirsiniz.

'scan_single' komutunu kullanarak sadece belirli bir ağın detaylarını tarayabilirsiniz.
Örnek kullanım:
   scan_single 90:4d:4a:6b:f5:a9
   (Bu, BSSID: 90:4d:4a:6b:f5:a9 olan ağın detaylarını gösterir.)
""")

def main():
    os.system('clear')  # Terminal ekranını temizler
    banner()

    # Monitor modunu kontrol et
    if not check_monitor_mode():
        print("HATA: Cihazınız monitor modunda değil!")
        print("Monitor moda geçiş yapmak için şu adımları izleyebilirsiniz:")
        print("1. Wi-Fi adaptörünüzün monitor moda geçişini sağlayın.")
        print("2. Aşağıdaki komutları kullanarak monitor moda geçebilirsiniz:")
        print("   sudo ip link set wlan0 down")
        print("   sudo iw dev wlan0 set type monitor")
        print("   sudo ip link set wlan0 up")
        print("\nMonitor moduna geçmeden işlem yapmanız mümkün değildir. Program sonlandırılıyor...")
        exit(1)
    else:
        print("Cihaz zaten monitor modunda.")
    
    while True:
        try:
            command = input("Komut girin: ").strip().lower()
            
            if command == "scan_wifi":
                scan_wifi()
            elif command.startswith("scan_single"):
                # Belirli bir ağın taranması için BSSID alır
                try:
                    _, target_bssid = command.split()
                    scan_single_network(target_bssid)
                except ValueError:
                    print("Hatalı komut formatı. Lütfen geçerli bir BSSID girin.")
                    print("Örnek: scan_single 90:4d:4a:6b:f5:a9")
            elif command == "help":
                help_command()
            elif command == "exit":
                print("Çıkılıyor...")
                exit(0)
            else:
                print("Geçersiz komut. Yardım için 'help' yazın.")
        except KeyboardInterrupt:
            print("\nProgram sonlandırıldı. Kullanıcı tarafından iptal edildi.")
            exit(0)
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            print("Komut işlenirken bir hata meydana geldi. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
