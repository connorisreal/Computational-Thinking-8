import random

def scramble_word(word):
   return "".join(random.sample(word, len(word)))

words = [
    "scone",
    "lizard",
    "magic",
    "ocean",
    "yeast",
    "queen",
    "ignite",
    "graze",
    "igloo",
    "tabby",
    "jester",
    "fable",
    "eight",
    "velvet",
    "acorn",
    "noble",
    "hinge",
    "pardon",
    "ridge",
    "maple",
    "rabble",
    "cellar",
    "bounce",
    "engage",
    "profit",
    "kiosk",
    "clever",
    "nimble",
    "zephyr",
    "joyful",
    "rocket",
    "lagoon",
    "fierce",
    "jingle",
    "mortal",
    "elbow",
    "gravel",
    "oyster",
    "delta",
    "plunge",
    "lively",
    "enrich",
    "willow",
    "garlic",
    "breeze",
    "quirky",
    "locket",
    "narrow",
    "clover",
    "sleek",
    "rescue",
    "throne",
    "hunter",
    "dagger",
    "ablaze",
    "jigsaw",
    "victor",
    "purple",
    "warmth",
    "donkey",
    "oxide",
    "rascal",
    "saddle",
    "quartz",
    "fallow",
    "prism",
    "karma",
    "noodle",
    "witty",
    "candor",
    "kitten",
    "giant",
    "piano",
    "nerve",
    "mosaic",
    "wander",
    "voyage",
    "lemon",
    "vapor",
    "pepper",
    "basket",
    "lumber",
    "zebra",
    "solar",
    "zipper",
    "frosty",
    "ultra",
    "waltz",
    "fluffy",
    "tablet",
    "herald",
    "quiver",
    "young",
    "happy",
    "quota",
    "mystic",
    "dangle",
    "dazzle",
    "uplift",
    "aching",
]
word = random.choice(words)
scrambled = scramble_word(word)

print("Scrambled word:", scrambled)

attempts = 3
while attempts > 0:
   guess = input("Guess the word: ").lower()
   if guess == word:
       print("Correct! Good job!")
       break
   else:
       attempts -= 1
       print(f"Wrong! {attempts} attempts left.")

if attempts == 0:
   print(f"Game over! The correct word was {word}.")