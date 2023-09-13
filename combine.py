from typing import Protocol

class Combinable(Protocol):
    def can_combine(self, other: "Combinable") -> bool:
        ...
    
    def combine(self, other: "Combinable") -> "Combinable":
        ...