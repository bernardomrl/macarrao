from domain.models import DependencyInjection, Injection
from domain.services.controllers import *
from domain.services.factories import *
from infrastructure.cozinhar_controllers.cozinhar_controller_fogao import (
    CozinharControllerFogao,
)
from infrastructure.encher_de_agua_controllers.encher_de_agua_controller_pia import (
    EncherDeAguaControllerPia,
)
from infrastructure.ferver_controllers.fever_controller_fogao import (
    FerverControllerFogao,
)
from infrastructure.macarrao_factories.macarrao_factory_espaguete import (
    MacarraoFactoryEspaguete,
)
from infrastructure.panela_factories.panela_factory_media import PanelaFactoryMedia


class CoreBridgeAdapter:
    def __init__(self):
        self.adapters = {
            "cozinhar_controller_fogao": CozinharControllerFogao(),
            "encher_de_agua_controller_pia": EncherDeAguaControllerPia(),
            "ferver_controller_fogao": FerverControllerFogao(),
            "macarrao_factory_espaguete": MacarraoFactoryEspaguete(),
            "panela_factory_media": PanelaFactoryMedia(),
        }

    def get_injection(
        self, dependency_injection: DependencyInjection
    ) -> Injection:
        return Injection(
            self.adapters[dependency_injection.cozinhar_controller],
            self.adapters[dependency_injection.encher_de_agua_controller],
            self.adapters[dependency_injection.ferver_controller],
            self.adapters[dependency_injection.macarrao_factory],
            self.adapters[dependency_injection.panela_factory],
        )
