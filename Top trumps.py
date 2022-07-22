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
    player_poke1 = random_pokemon()
    player_poke2 = random_pokemon()
    player_poke3 = random_pokemon()
    player_choice = int(input(f"Which Pokemon would you like to choose? \n 1: {player_poke1} \n 2: {player_poke2} \n "
                              f"3: {player_poke3}? "))
    possible_choices = [1, 2, 3]
    if player_choice not in possible_choices:
        print("Uh oh, please choose 1, 2 or 3")
    else:
        if player_choice == 1:
            player_poke = player_poke1
            print(f"You chose {player_poke}")
        elif player_choice == 2:
            player_poke = player_poke2
            print(f"You chose {player_poke}")
        elif player_choice == 3:
            player_poke = player_poke3
            print(f"You chose {player_poke}")
        computer_poke = random_pokemon()
        stat = str(input("Which stat would you like to use, id, height or weight? "))
        possible_stats = ["id", "height", "weight"]
        if stat not in possible_stats:
            print("Uh oh, please chose id, height or weight.")
        else:
            player_num = player_poke[stat]
            computer_num = computer_poke[stat]
            if player_num > computer_num:
                print("Yay, you win!")
            elif player_num < computer_num:
                print("Sorry, you lose :(")
                print(f"The computer's pokemon was: {computer_poke}")
            else:
                print("You draw!")
                print(f"The computer's pokemon was: {computer_poke}")


run()
