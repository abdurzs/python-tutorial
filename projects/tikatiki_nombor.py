import random

top_of_range = input("Tuliskan satu nombor: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Sila tulis satu nombor yang melebihi 0.")
        quit()
else:
    print("Sila tulis nombor sahaja.")
    quit()

random_number = random.randint(0, top_of_range)
teka = 0

while True:
    teka += 
    teka = input("Sila teka satu nombor: ")
    if teka.isdigit():
        teka = int(teka)
    else:
        print("Sila tulis nombor sahaja.")
        continue

    if teka == random_number:
        print("Tepat tekaan anda")
        break
    else:
        print("Cuba lagi.")

print("Anda berjaya menjawab dngn tepat!", + int(teka) +, "teka")