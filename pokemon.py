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
    # Taunt would be included here
    status: dict

    # Some moves like Wrap and Magma Storm continue to damage people
    affected_by_ongoing_move: dict

    # Some moves like Sky Attack or Solarbeam require two turns to set up
    setting_up_for_two_turn_move: bool

    # Launch a move, be it damaging or status
    def attack():
        pass

    # A switch
    # U-turn, Volt Switch, and Flip-Turn would all call this in additon to dealing damage
    def switch_out():
        pass

    # Put a substitute on the field to soak damage and prevent status
    def set_substitute():
        pass

    # Let the substitute take damage
    def damage_substitute():
        pass

    # Damage at the end of the turn due to weather
    def take_weather_damage():
        pass

    # Some statuses deal damage at the end of the turn
    def take_status_damage():
        pass