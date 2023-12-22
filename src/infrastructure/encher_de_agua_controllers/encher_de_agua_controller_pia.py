from domain.models import Panela
from domain.services.controllers import EncherDeAguaController


class EncherDeAguaControllerPia(EncherDeAguaController):
    def encher_panela_com_agua(self, panela: Panela) -> Panela:
        panela.agua = True
        return panela
