import numpy as np
import pandas as pd

from MAB.MAB_player import Player


class Slot_machine:
    def __init__(
        self,
        fail_chance,
        cost,
        win_multiplier,
        critical_success_threshold=None,
        critical_success_multiplier=None,
    ):
        assert (
            fail_chance > 0 and fail_chance < 1
        ), "fail_chance must be between 0 and 1"
        self.fail_chance = fail_chance
        assert cost > 0, "cost must be positive"
        self.cost = cost
        assert win_multiplier >= 1, "win_multiplier must be equal or greater than 1"
        self.win_multiplier = win_multiplier
        if critical_success_threshold and critical_success_multiplier:
            assert (
                critical_success_threshold > 0 and critical_success_threshold < 1
            ), "critical_success_threshold must be between 0 and 1"
            assert (
                critical_success_threshold > fail_chance
            ), "critical_success_threshold must be higher than fail_chance: {fail_chance}"
            self.critical_success_threshold = critical_success_threshold
            assert (
                critical_success_multiplier > win_multiplier
            ), "critical_success_multiplier must be higher than win_multiplier"
            self.critical_success_multiplier = critical_success_multiplier
        else:
            self.critical_success_threshold = None
            self.critical_success_multiplier = None

    def play_game(self, player: Player):
        result = np.random.uniform(0, 1, 1)
        player.play_game(self.cost)
        if result < self.fail_chance:
            print(f"{player.name} lost")
            return -self.cost
        else:
            if self.critical_success_threshold:
                if result > self.critical_success_threshold:
                    player.win(self.cost * self.critical_success_multiplier)
                    print(f"{player.name} won")
                    return self.cost * self.critical_success_multiplier
            player.win(self.cost * self.win_multiplier)
            print(f"{player.name} won")
            return self.cost * self.win_multiplier


slot_1 = Slot_machine(
    fail_chance=0.5,
    cost=1,
    win_multiplier=1.25,
)

slot_2 = Slot_machine(
    fail_chance=0.75,
    cost=1,
    win_multiplier=5,
)

slot_3 = Slot_machine(
    fail_chance=0.5,
    cost=1,
    win_multiplier=1.1,
    critical_success_threshold=0.9,
    critical_success_multiplier=20,
)
