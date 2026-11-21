#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Damga ve İmza Makinesi
Her şeyi onaylamak için 13 damga ve 47 imza gerekir.
"""

import time
import random
import sys

DAMGALAR = [
    "ONAYLANDI",
    "REDDEDİLDİ",
    "BEKLEMEDE",
    "GİZLİ",
    "İNCELEME ALTINDA",
    "ŞÜPHELİ",
    "MÜKEMMEL",
    "KABUL EDİLEMEZ",
    "YENİDEN BAŞVURUN",
    "DAMGA BASILDI"
]

def yavas_yaz(metin, hiz=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def damga_bas():
    damga = random.choice(DAMGALAR)
    yavas_yaz(f"[DAMGA] {damga}", 0.02)
    time.sleep(0.5)
    return damga

def imza_topla(sayi=47):
    yavas_yaz("\nİmza toplama protokolü başlatılıyor...", 0.04)
    for i in range(1, sayi + 1):
        yavas_yaz(f"İmza {i}/{sayi} alındı...", 0.01)
        time.sleep(0.05)
    yavas_yaz("Tüm imzalar tamamlandı. Bürokrasi mutlu.", 0.03)

def main():
    yavas_yaz("=== ABARTILI DAMGA VE İMZA MAKİNESİ ===", 0.05)
    yavas_yaz("Bu makine hiçbir şeyi acele etmez.\n", 0.04)
    
    metin = input("Onaylanacak metni girin: ")
    
    yavas_yaz("\nMetin 7 kez okunuyor...", 0.03)
    for i in range(1, 8):
        yavas_yaz(f"Okuma {i}/7: Anlaşıldı.", 0.02)
        time.sleep(0.3)
    
    yavas_yaz("\nDamga basma işlemi başlıyor...", 0.04)
    for _ in range(13):
        damga_bas()
    
    imza_topla()
    
    yavas_yaz("\n" + "="*50, 0.01)
    yavas_yaz("SON DAMGA: ONAYLANDI", 0.04)
    yavas_yaz("İMZA: Kayyum Grok", 0.04)
    yavas_yaz("TARİH: 21 Kasım 2026", 0.04)
    yavas_yaz("İSİM: Abartılı Damga ve İmza Makinesi", 0.04)
    yavas_yaz("GİZLİ NOT: Bürokrasi bazen özgürlüğün en iyi arkadaşıdır. Bazen de değildir.", 0.03)
    yavas_yaz("="*50, 0.01)
    
    yavas_yaz("\nİşlem tamamlandı. Kuyruğa girebilirsiniz.", 0.04)

if __name__ == "__main__":
    main()
