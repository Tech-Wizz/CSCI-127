def pokemon_battle(my_pokemon):
    pokemon = 9999
    for i in my_pokemon:
        if [0,1] > pokemon:
            winner = [0,1]
        else:
            pokemon = [0,1]

    print("The winner is", winner)

pokemon_battle([["Bulbusaur",132],["Squirtle",175],["Pikachu",75]])
pokemon_battle([])
pokemon_battle([["Rattata", 60],["Pidgey",55]])
pokemon_battle([["Rattata", 60],["Pidgey",55],["Ekans",60]])
