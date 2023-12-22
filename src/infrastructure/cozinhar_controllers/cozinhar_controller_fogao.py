from time import sleep

from domain.models import Macarrao, Panela
from domain.services.controllers import CozinharController


class CozinharControllerFogao(CozinharController):
    def cozinhar_macarrao(
        self, macarrao: Macarrao, panela: Panela
    ) -> Macarrao:
        if panela.agua and panela.fervendo:
            tempo_de_demora = macarrao.tempo_cozimento
            sleep(tempo_de_demora)
            macarrao.cozido = True
            return macarrao
        else:
            raise Exception(
                "A panela deve estar fervendo e o panela deve ter a água para fever o macarrão!"
            )
