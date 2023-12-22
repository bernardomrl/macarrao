from dataclasses import dataclass

from domain.services.controllers import CozinharController
from domain.services.controllers import FerverController
from domain.services.controllers import EncherDeAguaController

from domain.services.factories import MacarraoFactory
from domain.services.factories import PanelaFactory

@dataclass
class Injection:
    cozinhar_controller: CozinharController
    encher_de_agua_controller: EncherDeAguaController
    ferver_controller: FerverController
    macarrao_factory: MacarraoFactory
    panela_factory: PanelaFactory
