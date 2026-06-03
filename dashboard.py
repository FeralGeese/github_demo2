import random
print("super gaaf dashboard")
coin = ["Heads", "Tails"]
def flip_coin():
    coin_flip = random.choice(coin)
    print(coin_flip)
    if coin_flip.lower == "heads":
        print("Heads!")
flip_coin()

