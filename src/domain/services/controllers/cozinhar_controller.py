from domain.models.macarrao import Macarrao 
from domain.models.panela import Panela

class CozinharController:
    def cozinhar_macarrao(
        self, macarrao: Macarrao, panela: Panela
    ) -> Macarrao:
        raise NotImplementedError()
