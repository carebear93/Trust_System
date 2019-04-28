import random

from agent import Agent

class SimpleAgent(Agent):

    def __init__(self,env=None):
        super().__init__(environment=env)
        self.neighbor_interactions={}

    def pick_partner(self):
        max_trust=-2
        trusted=None
        for n in self.env.neighbors(self):
            #print (max_trust)
            #print (self.compute_trust(n))
            if max_trust<self.compute_trust(n):
                trusted=n
                max_trust=self.compute_trust(n)
        return trusted

    def pick_reference(self):
        max_trust=-2
        reference=None
        for n in self.env.neighbors(self):
            #print (max_trust)
            #print (self.compute_trust(n))
            if max_trust<self.compute_trust(n):
                reference=n
                max_trust=self.compute_trust(n)
        return reference

    def learn(self,n,success):
        if n not in self.neighbor_interactions:
            self.neighbor_interactions[n]=[0,0]
        if success:
            self.neighbor_interactions[n][0]+=1
        else:
            self.neighbor_interactions[n][1]+=1

    def learnRef(self,n,success):
        if n not in self.neighbor_interactions:
            self.neighbor_interactions[n]=[0,0]
        if success:
            self.neighbor_interactions[n][0]+=1
        else:
            self.neighbor_interactions[n][1]+=1

    def compute_trust(self,n):
        (s,f)=self.neighbor_interactions.get(n,(0,0))
        if (s+f)==0:
            return 0
        return (s-f)/(s+f+2)
