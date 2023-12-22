from dataclasses import dataclass


@dataclass
class Macarrao:
    tipo: str
    quantidade: int
    tempo_cozimento: int
    cozido: bool
