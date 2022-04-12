from dataclasses import dataclass, field

@dataclass(repr = True, init = True)
class Move():

    # Move's type
    type: str = field(default=None)
    
    # Move's power
    power: int = field(default=None)

    # Move's remaining power points
    pp: int = field(default=None)

    # A move could be multi-hit, like Pin Missile
    multihit: bool = field(default=False)

    # A move is either physical, special, or status
    physical_special_or_status: int = field(default=None)

    # Stats affected by a stat changing move
    stats_affected: dict = field(default={})

    # Some moves force a switch -> Roar
    forces_switch: bool = field(default=False)
