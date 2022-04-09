from dataclasses import dataclass


from dataclasses import dataclass

@dataclass(repr = True, init = True)
class Pokemon:

    # Pokemon's name
    name: str

    # Pokemon's ability
    ability: str

    # Pokemon's level
    level: int

    # First of two possible types
    type_one: str

    # Second of two possible types
    type_two: str

    # Current HP
    hp: int

    # Physical attack stat
    physical_attack: int

    # Physical defense stat
    physical_defense: int

    # Special attack stat
    special_attack: int

    # Special defense stat
    special_defense: int

    # Speed stat
    speed: int

    # Evasion stat
    evasion: int

    # Critical srike stage factor
    critical_strike_factor: int
    
    # The pokemon's set of four moves
    moves: dict

    # Stat modifications dictionary
        # I thought of this as a per-stat entry type of thing
        # IE 'physical_attack': 1 -> no change
    stat_modifications: dict

    # If a substitute is in play, it has its own HP stat, based on the pokemon who created it's HP
    substitute_up: dict

    # Only one type of status is possible at a time, but toxic has a special condition
    status: dict

    # Some moves like Wrap and Magma Storm continue to damage people
    affected_by_ongoing_move: dict

    # Some moves like Sky Attack or Solarbeam require two turns to set up
    setting_up_for_two_turn_move: dict

    def attack():
        pass

    def switch_out():
        pass

    def set_substitute():
        pass

    def damage_substitute():
        pass

    def take_weather_damage():
        pass

    def take_status_damage():
        pass

