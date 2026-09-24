from .distance_handler import DistanceHandler
from .dragon_alive_handler import DragonAliveHandler
from .perform_attack_handler import PerformAttackHandler


def create_attack_chain():
    distance = DistanceHandler()
    dragon_alive = DragonAliveHandler()
    perform_attack = PerformAttackHandler()
    distance.set_next(dragon_alive).set_next(perform_attack)
    return distance
