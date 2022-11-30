import pandas as pd
import numpy as np


class Player:
    def __init__(
        self,
        player_name: str,
        # list_of_slots,
        starting_money: int = 100,
    ):
        self.name = player_name
        self._starting_money = starting_money
        self._money = starting_money

    def reset(self):
        self._money = self._starting_money

    def win(self, winnings):
        self._money = self._money + winnings
        return self._money

    def play_game(self, cost):
        self._money = self._money - cost
        return self._money

    def __str__(self):
        return f"{self.name} has {self._money}$"
