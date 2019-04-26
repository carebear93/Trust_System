import random

from simple_agent import SimpleAgent

class SimpleReputationAgent(SimpleAgent):
    def get_trust(self,n):
        if random.random()>self.reputation_competence:
            return [random.randint(0,30),random.randint(0,30)]
        else:
            return self.neighbor_interactions.get(n,[0,0])

    def compute_trust(self,n):
        t=[0,0]
        for a in self.env.nodes:
            t=list(map(sum,zip(t,a.get_trust(n))))
        [s,f]=t
        return (s-f)/(s+f+2)
