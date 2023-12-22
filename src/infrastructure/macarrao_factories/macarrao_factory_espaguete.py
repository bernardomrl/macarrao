from domain.models import Macarrao
from domain.services.factories import MacarraoFactory


class MacarraoFactoryEspaguete(MacarraoFactory):
    def call(self, quantidade: int) -> Macarrao:
        return Macarrao("espaguete", quantidade, 10, False)
