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
print(random_number)