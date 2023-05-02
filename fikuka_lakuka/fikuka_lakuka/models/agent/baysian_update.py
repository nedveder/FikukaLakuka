import numpy as np

from fikuka_lakuka.fikuka_lakuka.models import History, ActionSpace
from fikuka_lakuka.fikuka_lakuka.models.agent.base import Agent
from fikuka_lakuka.fikuka_lakuka.models.i_state import IState


class BaysianBeliefAgent(Agent):

    def __init__(self, config_params: dict):
        self.config_params = config_params

    def act(self, state: IState, history: History) -> int:
        if state.rocks_set:
            rock_distances = self.calc_rock_distances(state)
            rock_distances[np.asarray(state.collected_rocks, dtype=bool)] = state.grid_size[0] * state.grid_size[1]
            min_rock = state.rocks_arr[np.argmin(rock_distances)]
            action = self.go_towards(state, min_rock)

            return action.value
        else:
            return self.go_towards(state, state.end_pt).value

    def update(self, reward: float, history: History):
        pass
