import random
import world.text.world
list_of_obstacles = []
is_position_blocked_list = []

def generate_random_obstacles():
    global list_of_obstacles
    num_of_obstacles = random.randint(1,10)
    list_of_obstacles = [(random.randint(-100,100),random.randint(-200,200))\
    for x in range(num_of_obstacles)]
    # print(is_position_blocked_list)
    return list_of_obstacles


def is_position_blocked(x,y):
    global list_of_obstacles
    # help from Aidan.

    for i,obs in enumerate(list_of_obstacles):
        if obs[0] <= x <= obs[0]+4 and obs[1] <= y <= obs[1]+4:
            return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    global list_of_obstacles
    for i, obs in enumerate(list_of_obstacles):
        if x1 == x2:
            if (y1 <=  obs[1] <= y2 or y1 >=  obs[1] >= y2) and\
            obs[0] <= x1 <= obs[0]:
                return True
        if y1 == y2:
            if (x1 <=  obs[0] <= x2 or x1 >=  obs[0] >= x2) and\
            obs[1] <= y1 <= obs[1]:
                return True
    return False
            

def get_obstacles():
    return list_of_obstacles