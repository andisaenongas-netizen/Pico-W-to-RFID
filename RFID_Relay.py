from machine import Pin
from mfrc522 import MFRC522
import utime

# Konfigurasi RFID RC522
reader = MFRC522(
    spi_id=0,
    sck=6,
    miso=4,
    mosi=7,
    cs=5,
    rst=22
)

# Konfigurasi Relay
relay1 = Pin(0, Pin.OUT)
relay2 = Pin(1, Pin.OUT)

# Kondisi awal relay OFF
relay1.value(0)
relay2.value(0)

# ID Card yang diizinkan
valid_card = 756663523

print("Dekatkan RFID TAG...")
print("")


while True:
    reader.init()

    (stat, tag_type) = reader.request(reader.REQIDL)

    if stat == reader.OK:

        (stat, uid) = reader.SelectTagSN()

        if stat == reader.OK:

            # Mengubah UID RFID menjadi angka
            card = int.from_bytes(bytes(uid), "little", False)

            print("Card ID :", card)

            # Jika kartu sesuai
            if card == valid_card:

                print("CARD VALID - Relay Aktif")

                # Aktifkan kedua relay
                relay1.value(1)
                relay2.value(1)

                utime.sleep(5)

                # Matikan kembali relay
                relay1.value(0)
                relay2.value(0)

                print("Relay OFF")


            else:
                print("UNKNOWN CARD - Akses Ditolak")

                # Pastikan relay mati
                relay1.value(0)
                relay2.value(0)

    utime.sleep(0.5)