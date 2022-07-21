import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


def run():
    player_poke = random_pokemon()
    computer_poke = random_pokemon()
    print(f"Your pokemon is: {player_poke}")
    stat = input("Which stat would you like to use, id, height or weight? ")
    if stat == "id":
        if player_poke["id"] > computer_poke["id"]:
            print("Congratulations, you win!")
        elif player_poke["id"] < computer_poke["id"]:
            print("Sorry, you lose :(")
            print(computer_poke)
        else:
            print("It's a draw")
    if stat == "height":
        if player_poke["height"] > computer_poke["height"]:
            print("Congratulations, you win!")
        elif player_poke["height"] < computer_poke["height"]:
            print("Sorry, you lose :(")
            print(computer_poke)
        else:
            print("It's a draw")
    if stat == "weight":
        if player_poke["weight"] > computer_poke["weight"]:
            print("Congratulations, you win!")
        elif player_poke["weight"] < computer_poke["weight"]:
            print("Sorry, you lose :(")
            print(computer_poke)
        else:
            print("It's a draw")

run()


