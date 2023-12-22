from dataclasses import dataclass


@dataclass
class DependencyInjection:
    cozinhar_controller: str
    encher_de_agua_controller: str
    ferver_controller: str
    macarrao_factory: str
    panela_factory: str
