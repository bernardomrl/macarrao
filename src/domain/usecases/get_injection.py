from domain.models import Injection
from domain.services.bridges import CoreBridge
from domain.services.factories import CoreDependencyInjectionFactory


class GetInjection:
    def __init__(
        self,
        core_bridge: CoreBridge,
        core_dependency_injection_factory: CoreDependencyInjectionFactory,
    ) -> None:
        self.core_bridge = core_bridge
        self.core_dependency_injection_factory = (
            core_dependency_injection_factory
        )

    def call(self) -> Injection:
        dependency_injection = self.core_dependency_injection_factory.call()
        return self.core_bridge.get_injection(dependency_injection)
