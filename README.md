# Wifi Scanner & Deauth Attack Tool

Bu Python projesi, Wi-Fi ağlarını taramak ve ağdan cihazları atmak için kullanılan iki araçtan oluşmaktadır.

## Özellikler

- **Wi-Fi Tarama**: Tüm Wi-Fi ağlarını tarayabilirsiniz.
- **Monitor Moduna Geçiş**: Wi-Fi adaptörünüzü monitör moduna alabilirsiniz.
- **Deauth Attack**: Belirli bir cihazı veya tüm cihazları ağdan atmak için deauth saldırısı yapabilirsiniz.

## Gereksinimler

- **Python 3.x**
- **airodump-ng** (Wi-Fi tarama için)
- **Sudo yetkileri**
- **Wi-Fi adaptörü** (Monitor modunu destekleyen)

## Kurulum

### Gereksinimleri Yükleyin:

```bash
sudo apt update
sudo apt install aircrack-ng

--------------------------------------------

Python Bağımlılıklarını Yükleyin:
pip install scapy
-------------------------------------

Programı Çalıştırın:
python3 wifi_scanner.py
python3 deauth_attack.py
---------------------------------------------

Kullanım
Wi-Fi Tarama
Wi-Fi ağlarını taramak için wifi_scanner.py dosyasını çalıştırabilirsiniz:

python3 wifi_scanner.py
----------------------------------------------

Deauth Attack
deauth_attack.py dosyası, belirli bir cihazı veya tüm cihazları ağdan atmak için kullanılır.

⚠️ Dikkat: Bazı Wi-Fi adaptörlerinde bu saldırı çalışmayabilir.

python3 deauth_attack.py
-------------------------------------------

Dikkat Edilmesi Gerekenler

Wi-Fi Adaptörü: Deauth saldırısı bazı Wi-Fi adaptörlerinde çalışmayabilir. Monitor modunu destekleyen bir adaptör kullanmanız gerekmektedir.
Sudo Yetkileri: Programın bazı bölümleri sudo yetkisi gerektirir. Lütfen çalıştırmadan önce gerekli izinlere sahip olduğunuzdan emin olun.


Bu proje MIT Lisansı ile lisanslanmıştır.

Sorumluluk
Bu araç yalnızca yasal ve etik testler için kullanılmalıdır. Kullanıcı, yazılımı sadece kendisinin yetkilendirilmiş olduğu ağlarda ve cihazlarda kullanmakla sorumludur. İzinsiz ağlara veya cihazlara saldırmak, yasalarla cezalandırılabilir bir suçtur. Bu yazılımın kötüye kullanımından kaynaklanan tüm sorumluluk kullanıcıya aittir. 🚫
