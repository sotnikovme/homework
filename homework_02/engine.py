from dataclasses import dataclass

@dataclass
class Engine:
    volume: int 
    pistons: int

    # def __init__(self, volume = 2, pistons = 6):
    #     self.volume = volume
    #     self.pistons = pistons  