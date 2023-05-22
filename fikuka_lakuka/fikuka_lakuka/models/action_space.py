import random
from enum import Enum
from typing import Optional, Any, Tuple

import gym
from pydantic import BaseModel

from config import config

NUM_OF_ACTIONS = 4


class Actions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    SAMPLE = 4

class Action(BaseModel):
    action_type: Actions
    rock_sample_loc: Optional[Tuple[int, int]] = None


    @staticmethod
    def sample():
        return Action(action_type=Actions(random.randint(0, NUM_OF_ACTIONS)))

class Observation(Enum):
    NO_OBS = -1
    BAD_ROCK=0
    GOOD_ROCK=1


class ActionSpace(gym.spaces.Space):

    def __init__(self):
        self.rocks_arr = config.get_in_game_context("environment", "rocks")
        self.num_of_actions = len(self.rocks_arr) + 4
        super(ActionSpace, self).__init__((1, self.num_of_actions), dtype=int)

    def sample(self, mask: Optional[Any] = None):
        return random.randint(1, self.num_of_actions)

    def contains(self, x) -> bool:
        pass

    @property
    def space(self):
        return self

    def __contains__(self, item: int):
        return 1 <= item <= self.num_of_actions
