import random
from agent import Agent

class RandomAgent(Agent):

    def __init__(self,env=None):
        super().__init__(environment=env)

    def pick_partner(self):
        return random.choice(list(self.env.neighbors(self)))
