import turtle
import robot
import world.obstacles
# screen = turtle.getscreen()

tur =turtle.Turtle()
# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left',\
'sprint']
move_commands = valid_commands[3:]

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#commands history
history = []

def draw_border():
    tur.color("red")
    # tur.hideturtle()
    tur.speed(-1)
    tur.penup()
    tur.setposition(min_x,min_y)
    tur.pendown()
    tur.forward(201)
    tur.left(90)
    tur.forward(401)
    tur.left(90)
    tur.forward(201)
    tur.left(90)
    tur.forward(401)
    tur.left(90)
    tur.penup()
    tur.setposition(0,0)
    tur.color("black")
    tur.left(90)


def draw_obstacles(lis):
    tur.color("red")
    tur.speed(-1)
    tur.penup()
    for i,obs in enumerate(lis):
        # print(lis[i])
        tur.setposition(lis[i][0],lis[i][1])
        tur.pendown()
        tur.forward(4)
        tur.right(90)
        tur.forward(4)
        tur.right(90)
        tur.forward(4)
        tur.right(90)
        tur.forward(4)
        tur.right(90)
        tur.penup()
        tur.setposition(0,0)
    tur.color("black")
    # print(lis,'tur')
    # print('obsticals generated')


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+\
    str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
        
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        if world.obstacles.is_position_blocked(new_x,new_y) == True:
            return None
        if world.obstacles.is_path_blocked(position_x,position_y,new_x,new_y)\
        == True:
            return None
        position_x = new_x
        position_y = new_y
        return True

    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    x = update_position(steps)
    if x:
        tur.pendown()
        tur.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif x != None and not x:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    elif x == None:
        return True, 'Sorry, there is an obstacle in the way.'

def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    x = update_position(-steps)
    if x:
        tur.pendown()
        tur.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif x != None:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    elif x == None:
        return True, 'Sorry, there is an obstacle in the way.'

def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
    tur.pendown()
    tur.right(90)
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
    tur.pendown()
    tur.left(90)
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)
