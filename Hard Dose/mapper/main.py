import numpy as np
import queue

def det_obstacles(file_path):
    obs = []
    with open(file_path,"r") as file:
        for line in file:
            val = list(map(int, line.split()))
            if len(val) == 4: #since a single line contains info reg n,e,s,w we're stoppin with 4 vals
                n,e,s,w = val
                obs.append((n,e))
                obs.append((-s,-w))
    return obs

def map(obs,goal):
    min_x = min([x for x, y in obs] + [goal[0], 0]) #to find the size of the map/arena
    max_x = max([x for x, y in obs] + [goal[0], 0])
    min_y = min([y for x, y in obs] + [goal[1], 0])
    max_y = max([y for x, y in obs] + [goal[1], 0])


    x_s, y_s = abs(min_x) , abs(min_y)
    w = max_x - min_x + 1
    h = max_y - min_y + 1
    arena = np.ones((width,height),dtype = int)

    for x,y in obs:
        arena[x + x_s , y + y_s] = 0

    return arena, x_s, y_s

def shortest_path(arena,start,goal,x_s,y_s):
    w , h = arena.shape
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = np.zeros_like(arena, dtype = bool)
    start_shift = (start[0] + x_s, start[1] + y_s)
    goal_shift = (goal[0] + x_s, goal[1] + y_s)

    q = queue.Queue()
    q.put(start_shift)
    visited[start_shift] = True

    while not q.empty():
        x,y = q.get()
        if (x,y) == goal_shift:
            break
    for dx,dy in dirs:
        prev = []
        nx, ny = x + dx, y + dy #brick's checkin it's neighbor's coords
        if 0<= nx <= width and 0<= ny <= height and arena[nx,ny] == 1 and not visited[nx, ny]: #makes sure that nx,ny are inside the bound region and it's free from obstacles
            q.put((nx, ny)) #throws the neighbor coords in the queue
            visited[nx, ny] == True
            prev[nx, ny] = (x,y)
        path = []
        current = goal_shift #reached the goal
        while current in prev:
            path.append(current[0] - x_s , current[1] - y_s)
            current = prev[current] #to find the shortest path, we're backtrackin to start from the goal
        path.reverse()

        return path
if __name__ == "__main__":
    file_path = input("ENter the path to .txt file which contains info regardin obstacles: ")
    goal_x, goal_y = map(int , input("Enter the coords of goal: ").split())
    obs = det_obstacles(file_path)
    goal = (goal_x, goal_y)
    arena,x_s, y_s = map(obs, goal)

    start = (0,0)
    path = shortest_path(arena,start, goal, x_s, y_s)
    print("The followin is the map of the arena where, 0 represents obstacles and 1 represents free")
    print(arena)

    print("Shortest path from startin line to goal is: ")
    print(path)
