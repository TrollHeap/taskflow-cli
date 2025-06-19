from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    DONE = "x"
    INTER = "~"
    REVIEW = "?"
    TODO = " "


@dataclass
class ChecklistItem:
    idx: int
    statut: Status
    texte: str
