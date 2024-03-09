print("Selamat datang Masta ke Kuiz Tika Tiki")

playing = input("Sudikah anda bermain? ")

if playing.lower() != "ya":
    quit()

print("Ok! Jom Tika Tiki :)")
markah = 0

jawab = input("Perkataan apa yang dieja salah dalam kamus? ")
if jawab.lower() == "salah":
    print("Tepat sekali!")
    markah += 1
else:
    print("Cuba lagi!")

jawab = input("Bom apakah yang tidak boleh meletup? ")
if jawab.lower() == "bomba":
    print("Tepat sekali!")
    markah += 1
else:
    print("Cuba lagi!")

jawab = input("Dalam banyak-banyak bunga, bunga apa warna hitam? ")
if jawab.lower() == "bunga tayar":
    print("Tepat sekali!")
    markah += 1
else:
    print("Cuba lagi!")

jawab = input("Katak diterbalikkan jadi katak. Kopi di terbalikkan jadi? ")
if jawab.lower() == "tumpah":
    print("Tepat sekali!")
    markah += 1
else:
    print("Cuba lagi!")

print("Mantap, anda dapat jawab " + str(markah) + " soalan dengan betul! ")
print("Kemah " + str((markah/4) * 100) + " % untuk anda!")