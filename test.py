import random
import networkx as nx

from env import Env
from brs_reputation_agent import BRSReputationAgent


answers = []
for i in range(0,100):
    answers.append(0)

random.seed(1)
env=Env(nx.erdos_renyi_graph(100,0.1,seed=1,directed=True))

mapping={}
for i in range(0,100):
    mapping[i]=BRSReputationAgent(env)

nx.relabel_nodes(env,mapping,copy=False)

for i in range(0,100):
    e = env.tick()
    print(e
    answers[1] += e
seed += 1
