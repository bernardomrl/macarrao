from domain.models import Panela
from domain.services.controllers import EncherDeAguaController, FerverController
from domain.services.factories import PanelaFactory


class FerverAgua:
    def __init__(
        self,
        panela_factory: PanelaFactory,
        encher_de_agua_controller: EncherDeAguaController,
        ferver_controller: FerverController,
    ):
        self.panela_factory = panela_factory
        self.encher_de_agua_controller = encher_de_agua_controller
        self.ferver_controller = ferver_controller

    def call(self) -> Panela:
        panela = self.panela_factory.call()

        panela_com_agua = (
            self.encher_de_agua_controller.encher_panela_com_agua(panela)
        )

        return self.ferver_controller.ferver_panela(panela_com_agua)
