from domain.models import Macarrao

class MacarraoFactory:
    def call(
        self,
        quantidade: int,
    ) -> Macarrao:
        raise NotImplementedError()
