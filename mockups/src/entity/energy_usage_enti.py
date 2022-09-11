from dataclasses import dataclass

@dataclass
class EnergyUsage():
    site_id: str
    from_time: str
    to_time: str
    energy: int