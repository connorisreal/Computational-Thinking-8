choices = ["a", "b", "c"]
cats = 0
dogs = 0
other = 0
print("Hello! Today we're doing a simple personality quiz!")
print("\nIt'll test if you're a cat or dog person. Or neither!")
print("\nLet's do it!\n")

print("For context, all of these questions will be a 'how much' question. A = a lot, B = a little, and C = not/none at all.")

answer1 = input("\nFirst question! How much energy do you have on an average day?\n").lower()
if answer1 not in choices:
    while True:
        answer1 = input("Invalid choice. Please say A, B, or C.").lower()
        if answer1 in choices:
            break
if answer1 == "a":
    dogs += 1
elif answer1 == "b":
    cats += 1
elif answer1 == "c":
    other += 1
answer1 = input("\nSecond question! How many pets do you have?\n").lower()
if answer1 not in choices:
    while True:
        answer1 = input("Invalid choice. Please say A, B, or C.").lower()
        if answer1 in choices:
            break
if answer1 == "a":
    cats += 1
elif answer1 == "b":
    dogs += 1
elif answer1 == "c":
    other += 1
answer1 = input("\nThird question! Do you prefer hard or soft surfaces? A = hard, B = soft, C = neither.\n").lower()
if answer1 not in choices:
    while True:
        answer1 = input("Invalid choice. Please say A, B, or C.").lower()
        if answer1 in choices:
            break
if answer1 == "a" or answer1 == "c":
    other += 1
elif answer1 == "b":
    cats += 1
    dogs += 1
answer1 = input("\nFourth question! How much time do you have?\n").lower()
if answer1 not in choices:
    while True:
        answer1 = input("Invalid choice. Please say A, B, or C.").lower()
        if answer1 in choices:
            break
if answer1 == "a":
    dogs += 1
elif answer1 == "b":
    cats += 2
elif answer1 == "c":
    other += 2

answer1 = input("\nFifth and final question! How much space do you have in your home? Just use 'A' or 'B' for this one.\n").lower()
if answer1 != "a" and answer1 != "b":
    while True:
        answer1 = input("Invalid choice. Please say A or B.").lower()
        if answer1 == "a" or answer1 == "b":
            break
if answer1 == "a":
    dogs += 2
    cats += 2
elif answer1 == "b":
    other += 2

print(f"Dog points: {dogs}")
print(f"Cat points: {cats}")
print(f"Other points: {other}")
if dogs > cats and dogs > other:
    print("\nYou are a dog person!")
elif cats > dogs and cats > other:
    print("\nYou are a cat person!")
elif other > dogs and other > cats:
    print("\nYou are neither a cat NOR a dog person!")
elif other == cats:
    print("\nYou are kind of a cat person!")
elif other == dogs:
    print("\nYou are kind of a dog person!")
else:
    print("You like both cats and dogs equally!")

print("\nI hope you had fun!")