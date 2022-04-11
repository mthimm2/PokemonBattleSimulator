from random import randint

attacking_type_table = {
    'normal': {
        'normal': 1,
        'fire': 1,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 1,
        'fighting': 1,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 1,
        'bug': 1,
        'rock': 0.5,
        'ghost': 0,
        'dragon': 1,
        'dark': 1,
        'steel': 0.5,
        'fairy': 1
    },
    'fire': {
        'normal': 1,
        'fire': 0.5,
        'water': 0.5,
        'electric': 1,
        'grass': 2,
        'ice': 2,
        'fighting': 1,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 1,
        'bug': 2,
        'rock': 0.5,
        'ghost': 1,
        'dragon': 0.5,
        'dark': 1,
        'steel': 2,
        'fairy': 1
    },
    'water': {
        'normal': 1,
        'fire': 2,
        'water': 0.5,
        'electric': 1,
        'grass': 0.5,
        'ice': 1,
        'fighting': 1,
        'poison': 1,
        'ground': 2,
        'flying': 1,
        'psychic': 1,
        'bug': 1,
        'rock': 2,
        'ghost': 1,
        'dragon': 0.5,
        'dark': 1,
        'steel': 1,
        'fairy': 1
    },
    'electric': {
        'normal': 1,
        'fire': 1,
        'water': 2,
        'electric': 0.5,
        'grass': 0.5,
        'ice': 1,
        'fighting': 1,
        'poison': 1,
        'ground': 0,
        'flying': 2,
        'psychic': 1,
        'bug': 1,
        'rock': 1,
        'ghost': 1,
        'dragon': 0.5,
        'dark': 1,
        'steel': 1,
        'fairy': 1
    },
    'grass': {
        'normal': 1,
        'fire': 0.5,
        'water': 2,
        'electric': 1,
        'grass': 0.5,
        'ice': 1,
        'fighting': 1,
        'poison': 0.5,
        'ground': 2,
        'flying': 0.5,
        'psychic': 1,
        'bug': 0.5,
        'rock': 2,
        'ghost': 1,
        'dragon': 0.5,
        'dark': 1,
        'steel': 0.5,
        'fairy': 1
    },
    'ice': {
        'normal': 1,
        'fire': 0.5,
        'water': 0.5,
        'electric': 1,
        'grass': 2,
        'ice': 0.5,
        'fighting': 1,
        'poison': 1,
        'ground': 2,
        'flying': 2,
        'psychic': 1,
        'bug': 1,
        'rock': 1,
        'ghost': 1,
        'dragon': 2,
        'dark': 1,
        'steel': 0.5,
        'fairy': 1
    },
    'fighting': {
        'normal': 2,
        'fire': 1,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 2,
        'fighting': 1,
        'poison': 0.5,
        'ground': 1,
        'flying': 0.5,
        'psychic': 0.5,
        'bug': 0.5,
        'rock': 2,
        'ghost': 0,
        'dragon': 1,
        'dark': 2,
        'steel': 2,
        'fairy': 0.5
    },
    'poison': {
        'normal': 1,
        'fire': 1,
        'water': 1,
        'electric': 1,
        'grass': 2,
        'ice': 1,
        'fighting': 1,
        'poison': 0.5,
        'ground': 0.5,
        'flying': 1,
        'psychic': 1,
        'bug': 1,
        'rock': 0.5,
        'ghost': 0.5,
        'dragon': 1,
        'dark': 1,
        'steel': 0,
        'fairy': 2
    },
    'ground': {
        'normal': 1,
        'fire': 2,
        'water': 1,
        'electric': 2,
        'grass': 0.5,
        'ice': 1,
        'fighting': 1,
        'poison': 2,
        'ground': 1,
        'flying': 0,
        'psychic': 1,
        'bug': 0.5,
        'rock': 2,
        'ghost': 1,
        'dragon': 1,
        'dark': 1,
        'steel': 2,
        'fairy': 1
    },
    'flying': {
        'normal': 1,
        'fire': 1,
        'water': 1,
        'electric': 0.5,
        'grass': 2,
        'ice': 1,
        'fighting': 2,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 1,
        'bug': 2,
        'rock': 0.5,
        'ghost': 1,
        'dragon': 1,
        'dark': 1,
        'steel': 0.5,
        'fairy': 1
    },
    'psychic': {
        'normal': 1,
        'fire': 1,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 1,
        'fighting': 2,
        'poison': 2,
        'ground': 1,
        'flying': 1,
        'psychic': 0.5,
        'bug': 1,
        'rock': 1,
        'ghost': 1,
        'dragon': 1,
        'dark': 0,
        'steel': 0.5,
        'fairy': 1
    },
    'bug': {
        'normal': 1,
        'fire': 0.5,
        'water': 1,
        'electric': 1,
        'grass': 2,
        'ice': 1,
        'fighting': 0.5,
        'poison': 0.5,
        'ground': 1,
        'flying': 0.5,
        'psychic': 2,
        'bug': 1,
        'rock': 1,
        'ghost': 0.5,
        'dragon': 1,
        'dark': 2,
        'steel': 0.5,
        'fairy': 0.5
    },
    'rock': {
        'normal': 1,
        'fire': 2,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 2,
        'fighting': 0.5,
        'poison': 1,
        'ground': 0.5,
        'flying': 2,
        'psychic': 1,
        'bug': 2,
        'rock': 1,
        'ghost': 1,
        'dragon': 1,
        'dark': 1,
        'steel': 0.5,
        'fairy': 1
    },
    'ghost': {
        'normal': 0,
        'fire': 1,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 1,
        'fighting': 1,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 2,
        'bug': 1,
        'rock': 1,
        'ghost': 2,
        'dragon': 1,
        'dark': 0.5,
        'steel': 0.5,
        'fairy': 1
    },
    'dragon': {
        'normal': 1,
        'fire': 1,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 1,
        'fighting': 1,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 1,
        'bug': 1,
        'rock': 1,
        'ghost': 1,
        'dragon': 2,
        'dark': 1,
        'steel': 0.5,
        'fairy': 0
    },
    'dark': {
        'normal': 1,
        'fire': 1,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 1,
        'fighting': 0.5,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 2,
        'bug': 1,
        'rock': 1,
        'ghost': 2,
        'dragon': 1,
        'dark': 0.5,
        'steel': 0.5,
        'fairy': 0.5
    },
    'steel': {
        'normal': 1,
        'fire': 0.5,
        'water': 0.5,
        'electric': 0.5,
        'grass': 1,
        'ice': 2,
        'fighting': 1,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 1,
        'bug': 1,
        'rock': 2,
        'ghost': 1,
        'dragon': 1,
        'dark': 1,
        'steel': 0.5,
        'fairy': 2
    },
    'fairy': {
        'normal': 1,
        'fire': 0.5,
        'water': 1,
        'electric': 1,
        'grass': 1,
        'ice': 1,
        'fighting': 2,
        'poison': 0.5,
        'ground': 1,
        'flying': 1,
        'psychic': 1,
        'bug': 1,
        'rock': 1,
        'ghost': 1,
        'dragon': 2,
        'dark': 2,
        'steel': 0.5,
        'fairy': 1
    }
}

def damage_calc(pokemon_attacking, pokemon_defending, pokemon_attacking_move_power, pokemon_attacking_move_type, physical_special_or_status, weather):

    '''
        Damage formula: https://bulbapedia.bulbagarden.net/wiki/Damage
    '''

    # Level dependency doesn't rely on any other factors
    level_dependency = ((2 * pokemon_attacking.level() / 5) + 2)
    
    # A simple ratio of the correct attacking stat to the correct defending stat
    attack_to_defense_ratio = 0

    # If a move is a status move, it won't deal damage directly, but is still subject to type checking
    if physical_special_or_status == 'status':
        
        pass

    # Otherwise, we can perform the calculation as normal
    else:
        
        if physical_special_or_status == 'physical':
            attack_to_defense_ratio = pokemon_attacking.attack() / pokemon_defending.defense()  
        
        else:
            attack_to_defense_ratio = pokemon_attacking.special_attack() / pokemon_defending.special_defense()

    # This forms the numerator of the fraction present in the damage calc formula
    numerator = level_dependency * pokemon_attacking_move_power * attack_to_defense_ratio

    # Then we perform the division by 50 and add two and call this "base damage"
    base_damage = (numerator / 50) + 2
    
    # Next we need to consider the effect that weather has on certain moves
    damage_with_weather = 0

    # Weather affects the damage dealt and has specific cases for specific moves
    # TODO: Add specific cases for moves/abilities
    if weather == 'rain' and pokemon_attacking_move_type == 'water':
        damage_with_weather = base_damage * 1.5

    elif weather == 'rain' and pokemon_attacking_move_type == 'fire':
        damage_with_weather = base_damage * 0.5
    
    elif weather == 'sun' and pokemon_attacking_move_type == 'fire':
        damage_with_weather = base_damage * 1.5

    elif weather == 'sun' and pokemon_attacking_move_type == 'water':
        damage_with_weather = base_damage * 0.5
    
    elif weather == 'hail' and pokemon_attacking_move_type == 'ice':
        damage_with_weather = base_damage * 1.5

    else:
        damage_with_weather = base_damage

    # Assume that the move didn't crit
    crit_factor = 1

    # Critical hits multiply the damage done by 1.5x if rolled
    # TODO: Add crit logic
    if randint(1, 1001) > 42:
        crit_factor = 3 if pokemon_attacking.ability() is 'Sniper' else 1.5
        
    return damage_dealt