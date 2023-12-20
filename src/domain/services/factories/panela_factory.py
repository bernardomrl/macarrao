from domain.models import Panela

class PanelaFactory:
    def call (self) -> Panela:
        raise NotImplementedError()
