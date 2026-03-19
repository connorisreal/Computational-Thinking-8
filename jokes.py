name = input("\nHi there. What's your name?\n")
print(f"Hi, {name}!")

print("What do you call a pile of cats?")
input()
print("A MEOW-ntain!")
input()
print("Clever, right?")

input()

kk = input("\nKnock knock.\n").lower()
if kk == ("who's there" or "who's there?"):
    t = input("\nTank.\n")
else:
    while True:
        kk = input("\nSay who's there please.\n").lower()
        if kk == ("who's there?" or "who's there"):
            t = input("\nTank.\n").lower()
            break
if t == ("tank who"):
    t = input("\nYou're welcome!\n")
else:
    while True:
        t = input("\nSay tank who please.\n").lower()
        if t == ("tank who" or "tank who?"):
            t = input("\nYou're welcome!\n")
            break

print("\nThis was fun, right?\n")
print("Well, see you next time!")