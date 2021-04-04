from pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.pokemon_obj = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in self.pokemon:
            return "This pokemon is already caught"

        self.pokemon.append(pokemon.name)
        self.pokemon_obj.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name not in self.pokemon:
            return "Pokemon is not caught"

        self.pokemon.remove(pokemon_name)
        self.find_obj(pokemon_name)
        return f"You have released {pokemon_name}"

    def find_obj(self, pokemon_name):
        for poke in self.pokemon_obj:
            if poke.name == pokemon_name:
                self.pokemon_obj.remove(poke)
                break

    def trainer_data(self):
        output = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for poke in self.pokemon_obj:
            output += '- ' + poke.pokemon_details() + '\n'
        return output.rstrip()


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
