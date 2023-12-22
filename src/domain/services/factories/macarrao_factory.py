from domain.models.macarrao import Macarrao


class MacarraoFactory:
    def call(
        self,
        quantidade: int,
    ) -> Macarrao:
        raise NotImplementedError()
