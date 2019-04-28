import random
import networkx as nx

from env import Env
from simple_reputation_agent import SimpleReputationAgent


answers = []
for i in range(0,200):
    answers.append(0)

random.seed(1)
env=Env(nx.erdos_renyi_graph(200,0.1,seed=1,directed=True))

mapping={}
for i in range(0,200):
    mapping[i]=SimpleReputationAgent(env)

nx.relabel_nodes(env,mapping,copy=False)

for i in range(0,200):
    e = env.tick()
    print(e)
    answers[i] += e
