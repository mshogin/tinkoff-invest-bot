from trade_system.strategies.change_and_volume_strategy import ChangeAndVolumeStrategy
from trade_system.strategies.base_strategy import IStrategy

__all__ = ("StrategyFactory")


class StrategyFactory:
    """
    Fabric for strategies. Put here new strategy.
    """
    @staticmethod
    def new_factory(strategy_name: str, *args, **kwargs) -> IStrategy:
        match strategy_name:
            case "ChangeAndVolumeStrategy":
                return ChangeAndVolumeStrategy(*args, **kwargs)
            case _:
                raise Exception(f"Strategy {strategy_name} is not supported")
