from domain.models import DependencyInjection


class CoreDependencyInjectionFactory:
    def call(self) -> DependencyInjection:
        raise NotImplementedError()
