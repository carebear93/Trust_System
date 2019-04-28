import random

from simple_reputation_agent import SimpleReputationAgent

"""
Task 1 - Assessment 3
Beta Reputation System
Kristian Care
"""
class BRSReputationAgent(SimpleReputationAgent):

        def get_trust(self,n):
            if random.random()>self.reputation_competence:
                return [random.randint(0,30),random.randint(0,30)]
            else:
                return self.neighbor_interactions.get(n,[0,0])

        def compute_trust(self,n):
            t=[0,0]
            for a in self.env.nodes:
                # Trust in the person im asking
                b = self.get_trust(a)
                # Get Trust of n
                c = a.get_trust(n)
                # Beta Formulation
                d = (2* b[0] * c[0])/((b[1] + 2) * (c[0] + c[1] +2)+ 2*b[0])
                e = (2* b[0] * c[1])/((b[1] + 2) * (c[0] + c[1] +2)+ 2*b[0])
                # Increment trust values
                t[0] += d
                t[1] += e
                #t=list(map(sum,zip(t,a.get_trust(n))))
                #
            [s,f]=t
            return (s-f)/(s+f+2)
