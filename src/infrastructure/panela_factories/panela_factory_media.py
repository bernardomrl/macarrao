from domain.models import Panela
from domain.services.factories import PanelaFactory


class PanelaFactoryMedia(PanelaFactory):
    def call(self) -> Panela:
        return Panela(20, False, False)
