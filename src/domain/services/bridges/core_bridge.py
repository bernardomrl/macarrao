from domain.models import DependencyInjection, Injection
from services.controllers import *
from services.factories import *

class CoreBridge:
    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
        raise NotImplementedError()