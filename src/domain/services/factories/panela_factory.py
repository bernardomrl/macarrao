from domain.models.panela import Panela


class PanelaFactory:
    def call(self) -> Panela:
        raise NotImplementedError()
