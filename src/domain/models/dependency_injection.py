from dataclasses import dataclass

from domain.services.controllers import *
from domain.services.factories import *


@dataclass
class DependencyInjection:
    cozinhar_controller: str
    encher_de_agua_controller: str
    ferver_controller: str
    macarrao_factory: str
    panela_factory: str