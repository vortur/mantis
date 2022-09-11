from dataclasses import dataclass

@dataclass
class Status():
    id: int
    created_at: str
    e_tag: str
    site_id: str
    status: str
    status_description: str