import json

from domain.models import DependencyInjection
from domain.services.factories import CoreDependencyInjectionFactory


class CoreDependencyInjectionFactoryJson(CoreDependencyInjectionFactory):
    def call(self) -> DependencyInjection:
        with open(
            "/home/bernardomrl/Documents/code/macarrao/utils/dependency_injections.json",
            "r",
        ) as f:
            dependency_injections = json.load(f)
            return DependencyInjection(
                dependency_injections["cozinhar_controller"],
                dependency_injections["encher_de_agua_controller"],
                dependency_injections["ferver_controller"],
                dependency_injections["macarrao_factory"],
                dependency_injections["panela_factory"],
            )
