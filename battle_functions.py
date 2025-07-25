# JSON files from https://github.com/LeoTieu/pokemon_data

import json


with open("data/all_type_interactions.json", "r") as file:
    type_interactions = json.load(file)
with open("data/pokemon_types.json", "r") as file:
    pokemon_type_dict = json.load(file)
with open("data/pokemons.json", "r") as file:
    pokemons = json.load(file)

def get_interactions(pokemon: str) -> dict:
    """Identifies battle interactions of a specific pokemon"""
    pokemon = pokemon.lower()
    if pokemon not in pokemon_type_dict:
        print("Pokemon not found. Please check again.")
        return # type: ignore
    pokemon_type =  pokemon_type_dict[pokemon]
    return type_interactions[pokemon_type]


def print_coverage_for_pokemon(pokemon: str) -> None:
    """Prints all type matchups against the pokemon."""
    pokemon = pokemon.lower()
    interactions = get_interactions(pokemon)
    print_coverage(interactions)


def print_coverage_for_type(type: str) -> None:
    """Prints type matchups against given type.
    
    Format required is "type_1 type_2"
    Undercase and lowercase does not matter.
    """
    type = type.lower()
    type = ", ".join(sorted(type.split()))
    intereractions = type_interactions[type]
    print_coverage(intereractions)


def print_coverage(interaction_dict: dict) -> None:
    print_interaction_message("4x damage from", interaction_dict["quadruple_damage_from"])
    print_interaction_message("2x damage from", interaction_dict["double_damage_from"])
    print_interaction_message("1/2 damage from", interaction_dict["half_damage_from"])
    print_interaction_message("1/4 damage from", interaction_dict["quarter_damage_from"])
    print_interaction_message("immunities", interaction_dict["no_damage_from"])


def print_interaction_message(label: str, interaction_list: list) -> None:
    """Prints a label followed by a list of a Pókemon types."""
    if len(interaction_list) == 0:
        print(f"{label}: None")
    else:
        print(f"{label}: ", end="")
        for type in interaction_list:
            print(type, end=" ")
        print("")


if __name__ == "__main__":
    print_coverage_for_type("water steel")
