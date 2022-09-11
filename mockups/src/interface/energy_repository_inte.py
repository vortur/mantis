from abc import ABC
from abc import abstractmethod

from src.entity.energy_generation_enti import EnergyGeneration
from src.entity.energy_usage_enti import EnergyUsage
from src.entity.current_usage_enti import CurrentUsage
from src.entity.current_generation_enti import CurrentGeneration

class EnergyRepositoryInterface(ABC):
    @abstractmethod
    def energy_generation(self) -> EnergyGeneration:
        ...

    @abstractmethod
    def energy_usage(self) -> EnergyUsage:
        ...

    @abstractmethod
    def current_usage(self) -> CurrentUsage:
        ...

    @abstractmethod
    def current_generation(self) -> CurrentGeneration:
        ...

