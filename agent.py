import random

class Agent:
    def __init__(self,competence=random.random(),reputation_competence=1,environment=None):
        self.env=environment
        self.competence=competence
        self.reputation_competence=reputation_competence

    def execute(self):
        return random.random()<self.competence

    def pick_partner(self):
        pass

    def learn(self,partner,success):
        pass
