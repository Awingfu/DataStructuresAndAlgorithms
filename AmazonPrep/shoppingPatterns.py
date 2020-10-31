# https://leetcode.com/discuss/interview-question/906481/
# REDO
from typing import List
from collections import defaultdict

class Graph(object):
  def __init__(self, vertex_count):
    self.vertex_count = vertex_count
    self.edges = defaultdict(set)
    self.degrees = defaultdict(int)

  def addEdge(self, u, v):
    self.edges[u].add(v)
    self.edges[v].add(u)
    self.degrees[u] += 1
    self.degrees[v] += 1
  
  def getDegree(self, u):
    return self.degrees[u]

def getMinScore(products_nodes: int, products_edges: int, products_from: List[int], products_to: List[int]) -> int:
  if products_nodes == 0:
    return 0

  graph = Graph(products_nodes)
  for i in range(len(products_from)):
    u = products_from[i]
    v = products_to[i]
    graph.addEdge(u,v)

  minScore = float('inf')

  print(graph.edges)

  for u in graph.edges.keys():
    u_edges = graph.edges[u]
    for v in u_edges:
      for w in graph.edges.keys():
        w_edges = graph.edges[w]
        if w == u or w == v:
          continue
        if u in w_edges and v in w_edges:
          print(u,v,w)
          totalDegrees = sum([graph.getDegree(x) for x in [u, v, w]]) - 6 # connecting edges
          minScore = min(minScore, totalDegrees)
  return -1 if minScore == float("inf") else minScore


test1 = getMinScore(5,6,[1,2,2,3,4,5], [2,4,5,5,5,6])
print(test1) # 3