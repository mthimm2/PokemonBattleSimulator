from dataclasses import dataclass, field
from utils import randint

@dataclass(repr = True, init = True)
class Pokemon:

    # Pokemon's name
    name: str = field(default = '')

    # Pokemon's ability
    ability: str = field(default = '')

    # Pokemon's level
    level: int = field(default = 0)

    # First of two possible types
    type_one: str = field(default = '')

    # Second of two possible types
    type_two: str = field(default = '')

    # Pokemon's max hp
    max_hp: int = field(default = 0)

    # Current HP, because we can't base %max damage off of current hp
    current_hp: int = field(default = 0)

    # Physical attack stat
    physical_attack: int = field(default = 0)

    # Physical defense stat
    physical_defense: int = field(default = 0)

    # Special attack stat
    special_attack: int = field(default = 0)

    # Special defense stat
    special_defense: int = field(default = 0)

    # Speed stat
    speed: int = field(default = 0)

    # Evasion stat
    evasion: int = field(default = 0)

    # Critical srike stage factor
    crit_factor: int = field(default = 0)
    
    # The pokemon's set of four moves
    moves: list = field(default = [])

    # Stat modifications dictionary
        # I thought of this as a per-stat entry type of thing
        # IE 'physical_attack': 1 -> no change
    stat_modifications: dict = field(
        default = {
            'attack': 1,
            'defense': 1,
            'special_attack': 1,
            'special_defense': 1,
            'speed': 1,
            'evasion': 1,
            'crit_factor': 1,
            'accuracy': 1,
        }
    )

    # If a substitute is in play, it has its own HP stat, based on the pokemon who created it's HP
    # substitute_up: dict

    # Only one type of status is possible at a time, but toxic has a special condition
    # Taunt would be included here
    status: dict = field(
        default = {
            'paralysis': 0,
            'freeze' : 0,
            'sleep' : 0,
            'burn': 0,
            'poison': 0,
            'toxic': 0,
            'faint': 0,
            'bound': 0,
        }
    )

    # Some moves like Wrap and Magma Storm continue to damage people
    # affected_by_ongoing_move: dict

    # Some moves like Sky Attack or Solarbeam require two turns to set up
    # setting_up_for_two_turn_move: bool

    # Pokemon's gender matters for certain abilities and Attract
    # gender: str

    # Before a pokemon can attack, we should check if it's hindered by paralysis, freeze, attract, etc.
    def immobilized_check(self, attacking_move):
        
        # If the pokemon is paralyzed
        if self.status['paralysis'] != 0:

            # One quarter of the time, they won't be able to move
            if(randint(1,100) <= 25):
                return 1

        # When we're frozen, if we use a fire move, we thaw, otherwise, we might stay frozen
        elif self.status['frozen'] != 0:
            if attacking_move.type == 'fire':
                self.status['frozen'] = 0
                return 0
            else:
                # 20% chance to thaw at the end of each turn
                if(randint(1,100) <= 20):
                    self.status['frozen'] = 0
                    return 0
                else:
                    return 1

        # Sleep lasts for between 2 and 5 turns. So we can just decrement the sleep counter and wake up once equal to 0
        elif self.status['sleep'] != 0:
            self.status['sleep'] -= 1
            return 1
        
        # If you're not frozen or paralyzed, you're free to move (for now)
        else:
            return 0


    # Launch a move, be it damaging or status
    def choose_move(self):

        # From the standard turn interface, we would select attack, then choose a move.
        # That move will be returned and the damage calculation will take place in the context of the turn.
        # The reason for this is that it doesn't seem right for a pokemon to directly access the other's HP, etc.
        # An intermediate entity seems more appropriate in that case.
        while selected_move := input(f'1. {self.moves[0]}\t 2. {self.moves[0]}\t 3. {self.moves[0]}\t 4. {self.moves[0]}\t') not in [1,2,3,4]:
            print("Invalid move selection! Try again!")
        
        # Adjust for indexing
        return self.moves[selected_move - 1]

    # Put a substitute on the field to soak damage and prevent status
    # def set_substitute(self):

    #     # After reading about this on bulbapedia, the substitute just gets 1/4 of the HP of the pokemon that used it
    #     self.substitute_up['status'] = 1
    #     self.substitute_up['substitute_hp'] = self.hp // 4

    # Let the substitute take damage
    # def damage_substitute(self):
    #     pass

    # # Damage at the end of the turn due to weather
    # def take_weather_damage(self):
    #     pass

    # Some statuses deal damage at the end of the turn
    def take_status_damage(self):

        # At the end of a turn status damage is applied
        # Also, if a pokemon has one status condition, they cannot have another
        if self.status['burn'] == 1:
            self.current_hp -= self.max_hp // 16

        # Poison is a simple 1/8 hp per turn deduction
        elif self.status['poison'] == 1:
            self.current_hp -= self.max_hp // 8

        # Toxic is unique in that it's damage ramps up over time
        # Starting at 1/16, it increases linearly each turn: 2/16, 3/16, etc.
        # If the Pokemon that is toxic'd is switched out, that turn count resets.
        elif self.status['toxic'] != 0:
            self.current_hp -= (self.status['toxic'] * self.max_hp) // 16
            self.status['toxic'] += 1

        elif self.status['bound'] != 0:
            # TODO: Add logic to handle binding moves removing 1/8 per turn
            pass

    # Once you're at or below 0 hp, you're fainted
    def faint_check(self):

        # Fainting happens when hp == 0
        if self.hp <= 0:

            # This should be sufficient for checking for switches to a fainted pokemon as well
            self.status['faint'] = 1

            # Just because it'd be weird to have negative hp
            self.current_hp = 0

        