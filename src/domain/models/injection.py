from dataclasses import dataclass

from domain.services.controllers import *
from domain.services.factories import *


@dataclass
class Injection:
    cozinhar_controller: CozinharController
    encher_de_agua_controller: EncherDeAguaController
    ferver_controller: FerverController
    macarrao_factory: MacarraoFactory
    panela_factory: PanelaFactory