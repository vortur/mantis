from dataclasses import dataclass

@dataclass
class EnergyGeneration():
    from_time: str
    to_time: str
    site_id: int
    energy: int
