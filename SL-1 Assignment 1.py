graph = {
0: [1, 2],
1: [0, 3, 4],
2: [0,3],
3: [1,2,4],
4: [1,3]
}
x=int(input("How many Nodes are there in the graph :"))
visited=[0]*x #visited=[0,0,0,0,0]
def dfs(graph, s):#actual GRAPH ani STARTING vertex eg.0
visited[s]=1 #visited[0]=1 ==[1,0,0,0,0]
print(s)
for c in graph[s]:
if visited[c]==0:
dfs(graph,c)
def bfs(graph,s):
Queue=[s] #queue=[0]
visitedd=[s] #visitedd=[0]
while Queue: #until Queue contains some values
cur=Queue.pop(0)
print(cur)
for c in graph[cur]:
if c not in visitedd:
Queue.append(c)
visitedd.append(c)
p=int(input("Choose DFS OR BFS :\n1).DFS\n2).BFS\n---->"))
if p==1:
dfs(graph,0)                  
if p==2:
bfs(graph,0)
