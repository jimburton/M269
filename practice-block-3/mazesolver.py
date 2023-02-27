# https://levelup.gitconnected.com/solve-a-maze-with-python-e9f0580979a1

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
    
start = 1, 1
end = 2, 5

solution = []
for i in range(len(maze)):
    solution.append([])
    for j in range(len(maze[i])):
        solution[-1].append(0)
i,j = start
solution[i][j] = 1

def make_step(k):
  for i in range(len(solution)):
    for j in range(len(solution[i])):
      if solution[i][j] == k:
        if i>0 and solution[i-1][j] == 0 and maze[i-1][j] == 0:
          solution[i-1][j] = k + 1
        if j>0 and solution[i][j-1] == 0 and maze[i][j-1] == 0:
          solution[i][j-1] = k + 1
        if i<len(solution)-1 and solution[i+1][j] == 0 and maze[i+1][j] == 0:
          solution[i+1][j] = k + 1
        if j<len(solution[i])-1 and solution[i][j+1] == 0 and maze[i][j+1] == 0:
           solution[i][j+1] = k + 1

k = 0
while solution[end[0]][end[1]] == 0:
    k += 1
    make_step(k)

i, j = end
k = solution[i][j]
the_path = [(i,j)]
while k > 1:
  if i > 0 and solution[i - 1][j] == k-1:
    i, j = i-1, j
    the_path.append((i, j))
    k-=1
  elif j > 0 and solution[i][j - 1] == k-1:
    i, j = i, j-1
    the_path.append((i, j))
    k-=1
  elif i < len(solution) - 1 and solution[i + 1][j] == k-1:
    i, j = i+1, j
    the_path.append((i, j))
    k-=1
  elif j < len(solution[i]) - 1 and solution[i][j + 1] == k-1:
    i, j = i, j+1
    the_path.append((i, j))
    k -= 1
    
