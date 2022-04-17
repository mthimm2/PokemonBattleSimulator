from dataclasses import dataclass, field

@dataclass(repr = True, init = True)
class Move:

    # Move's gotta have a name
    name: str = field(default='')

    # Move's type
    type: str = field(default='')
    
    # Move's power
    power: int = field(default=0)

    # Move's remaining power points
    pp: int = field(default=0)

    # A move could be multi-hit, like Pin Missile
    multihit: bool = field(default=False)

    # Some moves can flinch
    can_flinch: bool = field(default=False)

    # If a move can flinch, it has a flinch rate
    flinch_rate: int = field(default=0)

    # A move is either physical, special, or status
    physical_special_or_status: int = field(default=0)

    # Stats affected by a stat changing move
    stats_affected: dict = field(default_factory=dict)

    # Some moves force a switch -> Roar
    forces_switch: bool = field(default=False)
