import gym

from config import config
from fikuka_lakuka.fikuka_lakuka.models.i_state import IState
from fikuka_lakuka.fikuka_lakuka.models.action import Action
from fikuka_lakuka.fikuka_lakuka.models.history import History
from fikuka_lakuka.fikuka_lakuka.models.agent import init_agent
from fikuka_lakuka.fikuka_lakuka.models.agent.base import Agent


class RobotsEnv_v0(gym.Env):
    MAX_STEPS = 100
    def __init__(self):
        super()
        self.state = IState()
        self.action = Action()
        self.observation_space = self.state.space
        self.action_space = self.action
        self.history = History()
        self.agents = [init_agent(agent_id) for agent_id in config.get_in_game_context("playing_agents")]
        self._cur_agent_idx = 0

    @property
    def cur_agent(self)->Agent:
        return self.agents[self._cur_agent_idx]
    def next_agent(self):
        self._cur_agent_idx = (self._cur_agent_idx + 1) % len(self.agents)

    def step(self, action):
        assert action in self.action_space
        self.cur_agent.act()

    def reset(self, **kwargs):
        self.state = IState()

    def sample(self):
        action = self.cur_agent.act(self.history)
        return action.space

    def render(self, mode='human', close=False):
        self.state.print()

