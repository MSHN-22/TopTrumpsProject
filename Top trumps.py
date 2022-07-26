import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'experience': pokemon['base_experience'],
    }


def run():
    game = 5  # The number of rounds to play
    player_score = 0
    computer_score = 0
    while game > 0:
        player_poke1 = random_pokemon()  # Generates 3 random pokemon for the player to choose from
        player_poke2 = random_pokemon()
        player_poke3 = random_pokemon()
        player_choice = int(input(f"Which Pokemon would you like to choose? \n 1: {player_poke1} \n 2: {player_poke2}"
                                  f" \n 3: {player_poke3}? "))
        possible_choices = [1, 2, 3]
        if player_choice not in possible_choices:  # Checks whether choice is inputted correctly
            print("Uh oh, you must choose 1, 2 or 3")
            break
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
            possible_stats = ["weight", "height", "experience"]
            if game % 2 == 0:  # for even rounds the computer chooses a random stat to play
                stat = random.choice(possible_stats)
                print(f"The computer chose to play {stat}")
            else:  # for odd rounds the player chooses the stat to play
                stat = str(input("Which stat would you like to use, height, weight or experience? "))
                if stat not in possible_stats:  # Checks whether stat is inputted correctly
                    print("Uh oh, you must chose height, weight or experience.")
                    break
            player_num = player_poke[stat]
            computer_num = computer_poke[stat]
            if player_num > computer_num:
                print("Yay, you win!")
                player_score += 1
                game = game - 1  # keeps track of number of rounds played
                print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                      f"more round(s) to play.")
            elif player_num < computer_num:
                print("Sorry, you lose :(")
                print(f"The computer's pokemon was: {computer_poke}")
                computer_score += 1
                game = game - 1
                print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                      f"more round(s) to play.")
            else:
                print("You draw!")
                print(f"The computer's pokemon was: {computer_poke}")
                game = game - 1
                print(f"Your score is: {player_score}, the computer's score is: {computer_score}. You have {game} "
                      f"more round(s) to play.")
    if game == 0:  # Triggered after 5 rounds of play
        if player_score > computer_score:
            print(f"Congratulations, you beat the computer! Your score was {player_score}, the computer only scored "
                  f"{computer_score}!")
        elif computer_score > player_score:
            print(f"Uh oh, you got beaten by a computer. The computer scored {computer_score}, and you only got "
                  f"{player_poke} :(")


run()
