from domain.models import Macarrao, Panela
from domain.services.controllers import CozinharController
from domain.services.factories import MacarraoFactory


class CozinharMacarrao:
    def __init__(
        self,
        macarrao_factory: MacarraoFactory,
        cozinhar_controller: CozinharController,
    ):
        self.macarrao_factory = macarrao_factory
        self.cozinhar_controller = cozinhar_controller

    def call(
        self,
        panela: Panela,
        quantidade: int,
    ) -> Macarrao:
        macarrao = self.macarrao_factory.call(
            quantidade,
        )
        return self.cozinhar_controller.cozinhar_macarrao(macarrao, panela)
