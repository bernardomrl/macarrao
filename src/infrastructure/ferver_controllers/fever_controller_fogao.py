from domain.models import Panela
from domain.services.controllers import FerverController


class FerverControllerFogao(FerverController):
    def ferver_panela(self, panela: Panela) -> Panela:
        if panela.agua:
            panela.fervendo = True
            return panela
        else:
            raise Exception("A panela deve ter a água para fazer a fervura!")
