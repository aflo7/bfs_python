from queue import Queue
import datetime


def bfs(graphname, adjList, s, t):
  start_time = datetime.datetime.now()
  
  s.color = "Gray"
  s.distance = 0
  q = Queue(maxsize=0) # infinite sized queue
  q.put(s)
  while not q.empty():
    u = q.get()
    for v in adjList[u]:
      if v.color == "White":
        v.color = "Gray"
        v.distance = u.distance + 1
        v.pi = u
        q.put(v)
    u.color = "Black"
  end_time = datetime.datetime.now()
  elapsed = (end_time - start_time).total_seconds() * 1000
  if (t.distance == float('inf')):
    print("Graph:", graphname, "| There is no path from s to t.", "| Elapsed Time:", elapsed, "ms")
    return
  print("Graph:", graphname, "| Distance from s to t:", t.distance, "| Elapsed Time:", elapsed, "ms")