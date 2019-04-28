import networkx as nx
class Env(nx.DiGraph):
    def __init__(self,graph):
        super().__init__()
        self.add_nodes_from(graph)
        self.add_edges_from(graph.edges)

    def __str__(self):
        return

    def tick(self):
        num_succ=0
        for n in self.nodes:
            p=n.pick_partner()
            succ=p.execute()
            if succ:
                num_succ+=1
            n.learn(p,succ)
        return num_succ
