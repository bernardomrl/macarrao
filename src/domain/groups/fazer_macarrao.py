from domain.models.macarrao import Macarrao
from domain.usecases.cozinhar_macarrao import CozinharMacarrao
from domain.usecases.ferver_agua import FerverAgua
from domain.usecases.get_injection import GetInjection
from infrastructure.core_bridge_adapters import CoreBridgeAdapter
from infrastructure.core_dependency_injections_factories import (
    CoreDependencyInjectionFactoryJson,
)


def fazer_macarrao_group(quantidade: int) -> Macarrao:
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    core_bridge = CoreBridgeAdapter()

    get_injection = GetInjection(
        core_bridge, core_dependency_injection_factory
    )

    injection = get_injection.call()

    ferver_agua = FerverAgua(
        injection.panela_factory,
        injection.encher_de_agua_controller,
        injection.ferver_controller,
    )

    panela = ferver_agua.call()

    cozinhar_macarrao = CozinharMacarrao(
        injection.macarrao_factory,
        injection.cozinhar_controller,
    )

    return cozinhar_macarrao.call(panela, quantidade)
