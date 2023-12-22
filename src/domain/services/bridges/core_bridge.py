from domain.models.injection import Injection
from domain.models.dependency_injection import DependencyInjection


class CoreBridge:
    def get_injection(
        self, dependency_injection: DependencyInjection
    ) -> Injection:
        raise NotImplementedError()
