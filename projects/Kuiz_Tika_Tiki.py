print("Selamat datang Masta ke Kuiz Tika Tiki")

playing = input("Sudikah anda bermain? ")

if playing.lower() != "ya":
    quit()

print("Ok! Jom Tika Tiki :)")

jawab = input("Perkataan apa yang dieja salah dalam kamus? ")
if jawab.lower() == "salah":
    print("Tepat sekali!")
else:
    print("Cuba lagi!")

jawab = input("Bom apakah yang tidak boleh meletup? ")
if jawab.lower() == "bomba":
    print("Tepat sekali!")
else:
    print("Cuba lagi!")

jawab = input("Dalam banyak-banyak bunga, bunga apa warna hitam? ")
if jawab.lower() == "bunga tayar":
    print("Tepat sekali!")
else:
    print("Cuba lagi!")

jawab = input("Katak diterbalikkan jadi katak. Kopi di terbalikkan jadi? ")
if jawab.lower() == "tumpah":
    print("Tepat sekali!")
else:
    print("Cuba lagi!")