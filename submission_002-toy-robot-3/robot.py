"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint'\
,'replay']

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# list to save commands
history_list = []

digits = None
n = None
m = None


def get_robot_name():
    """[gets the name of the robot]

    Returns:
        [string]: [name of robot]
    """
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
    append_history(command)
    return command.lower()


def append_history(command):
    """[adds commands to a list to make a history list]

    Args:
        command (string): [commands the user enters]
    """
    global history_list
    (command_name, arg1) = split_command_input(command)
    vc = valid_command(command)
    if vc == True and command_name.lower() != 'help' and command_name.lower()\
    != 'off' and command_name.lower() != 'replay':
        history_list.append(command.lower())
        # print(history_list)


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split( )
    # print(args)
    if len(args) > 1 and len(args) < 3:
        return args[0].lower(), args[1].lower()
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    (command_name, arg1) = split_command_input(command)

    return command_name.lower() in valid_commands and (len(arg1) == 0 or\
    is_int(arg1)) or arg1 == 'silent' or arg1 == 'reversed' or arg1 == '3-1'\
        or arg1 == '3-2' or arg1 == '2-1' or arg1 == '4-1' or arg1 == '4-2'\
        or arg1 == '4-3'or arg1 == '5-1' or arg1 == '5-2' or arg1 == '5-3'\
        or arg1 == '5-4' or arg1 == '6-1' or arg1 == '6-2' or arg1 == '6-3'\
        or arg1 == '6-4' or arg1 == '6-5'


def output(name, message):
    """[outputs robot name and message]

    Args:
        name ([string]): [name of the robot]
        message ([string]): [message to be printed to terminal]
    """
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
"""


def show_position(robot_name):
    """[shows the current possition of robot]

    Args:
        robot_name ([string]): [name of robot]
    """
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
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

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


def do_replay(robot_name,command):
    '''
    plays all commands previously inputted by user
    '''
    global history_list
    global n
    for x in history_list:
        handle_command_replay(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(len(history_list))+\
    ' commands.'


def do_replay_silent(robot_name,command):
    '''
    plays all commands previously inputted by user
    '''
    global history_list
    for x in history_list:
        handle_command_replay_silent(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(len(history_list))+\
    ' commands silently.'


def do_replay_reversed(robot_name,command):
    '''
    plays all commands previously inputted by user
    '''
    global history_list
    history_list.reverse()
    for x in history_list:
        handle_command_replay_reversed(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(len(history_list))+\
    ' commands in reverse.'


def do_replay_reversed_silent(robot_name,command):
    '''
    plays all commands previously inputted by user
    '''
    global history_list
    history_list.reverse()
    for x in history_list:
        handle_command_replay_reversed_silent(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(len(history_list))+\
    ' commands in reverse silently.'


def do_replay_n(robot_name,command):
    '''
    function called when replay x amount of commands is required to end
    '''
    global history_list
    global n
    for x in history_list[-n:]:
        handle_command_replay(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n)+' commands.'


def do_replay_n_m(robot_name,command):
    '''
    function called when replay specific x amount of commands is required
    '''
    global history_list
    global n
    global m
    for x in history_list[-n:-m]:
        handle_command_replay(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n-m)+' commands.'


def do_replay_silent_n(robot_name,command):
    '''
    function called when replay silent x amount of commands is required
    '''
    global history_list
    global n
    # print (history_list)
    for x in history_list[-n:]:
        handle_command_replay_silent(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n)+' commands silently.'


def do_replay_silent_n_m(robot_name,command):
    '''
    function called when replay silent specific x amount of commands is required
    '''
    global history_list
    global n
    global m
    for x in history_list[-n:-m]:
        handle_command_replay_silent(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n-m)+' commands silently.'


def do_replay_reversed_n(robot_name,command):
    '''
    function called when replay reversed x amount of commands is required
    '''
    global history_list            
    global n
    history_list.reverse()
    # print (history_list)
    for x in history_list[-n:]:
        handle_command_replay_reversed(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n)+' commands in reverse.'


def do_replay_reversed_n_m(robot_name,command):
    '''
    function called when replay reversed specific x amount of commands is required
    '''
    global history_list
    global n
    global m
    for x in history_list[-n:-m]:
        handle_command_replay_reversed(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n-m)+' commands in reverse.'


def do_replay_reversed_silent_n(robot_name,command):
    '''
    function called when replay reversed silent x amount of commands is required
    '''
    global history_list            
    global n
    history_list.reverse()
    for x in history_list[-n:]:
        handle_command_replay_reversed_silent(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n)+\
        ' commands in reverse silently.'


def do_replay_reversed_silent_n_m(robot_name,command):
    '''
    function called when replay reversed silent specific x amount of commands is required
    '''
    global history_list
    global n
    global m
    for x in history_list[-n:-m]:
        handle_command_replay_reversed(robot_name,x)
    return True, ' > '+robot_name+' replayed '+str(n-m)+\
        ' commands in reverse silently.'


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot1
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global digits
    global n
    global m
    l = False
    if command[0:6] != 'replay':
        (command_name, arg) = split_command_input(command)

        if command_name == 'off':
            return False
        elif command_name == 'help':
            (do_next, command_output) = do_help()
            print(command_output)
            return do_next
        elif command_name == 'forward':
            (do_next, command_output) = do_forward(robot_name, int(arg))
            print(command_output)
            show_position(robot_name)
            return do_next
        elif command_name == 'back':
            (do_next, command_output) = do_back(robot_name, int(arg))
            print(command_output)
            show_position(robot_name)
            return do_next
        elif command_name == 'right':
            (do_next, command_output) = do_right_turn(robot_name)
            print(command_output)
            show_position(robot_name)
            return do_next
        elif command_name == 'left':
            (do_next, command_output) = do_left_turn(robot_name)
            print(command_output)
            show_position(robot_name)
            return do_next
        elif command_name == 'sprint':
            (do_next, command_output) = do_sprint(robot_name, int(arg))
            print(command_output)
            show_position(robot_name)
            return do_next
        # print(command_output)
        # show_position(robot_name)
        # return do_next

    elif command[0:6] == 'replay':
        temp = command.split(' ')
        temp.reverse()
        # print(temp[0][0:1])
        # print(command[0:17])
        # print(temp)
        for x in temp:
            if x[0].isdigit():
                digits = x
                if '-' in digits:
                    nums = [int(x) for x in digits.split('-')]
                    n, m = nums[0], nums[1]
                else:
                    n = int(digits)
                # print(n, m)
                l = True
        if command[0:14] == 'replay silent ' and command[14:17] != type(int):
            if isinstance(temp[0][0:1],str) and l == False:
                print(robot_name+':', "Sorry, I did not understand '"+\
                command[0:13].upper()+' '+command[14:17]+"'.")
                l = True
                return True
        if command[0:6] == 'replay' and command[8:8] == type(int) and command[9:] == 'reversed':
            print(789)
    (command_name, arg) = split_command_input(command)

    # replay reversed silent n-m
    if command_name.lower() =='replay' and 'reversed silent' in command.lower() and\
        n != None and m != None:
        (do_next,command_output) = do_replay_reversed_silent_n_m(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay reversed silent n
    elif command_name.lower() =='replay' and 'reversed silent' in command.lower() and\
        n != None and m == None:
        (do_next,command_output) = do_replay_reversed_silent_n(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay reversed n-m
    elif command_name.lower() =='replay' and 'silent' not in command.lower() \
        and 'reversed' in command.lower() and n != None and m != None:
        (do_next,command_output) = do_replay_reversed_n_m(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay reversed n
    elif command_name.lower() =='replay' and 'silent' not in command.lower() \
        and 'reversed' in command.lower() and n != None and m == None:
        (do_next,command_output) = do_replay_reversed_n(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay silent n-m
    elif command_name.lower() =='replay' and 'reversed' not in command.lower() \
        and 'silent' in command.lower() and n != None and m != None:
        (do_next,command_output) = do_replay_silent_n_m(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay_silent_n
    elif command_name.lower() =='replay' and 'reversed' not in command.lower() \
        and 'silent' in command.lower() and n != None and m == None:
        # print('lll')
        if l:
            (do_next,command_output) = do_replay_silent_n(robot_name,command)
            # print(do_next)
            print(command_output)
            show_position(robot_name)
            return do_next
    # replay n-m
    elif (command_name.lower() == 'replay' and 'silent' not in command.lower() \
        and 'reversed' not in command.lower() and n != None and m != None):
        (do_next,command_output) = do_replay_n_m(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay n
    elif (command_name.lower() == 'replay' and 'silent' not in command.lower() \
        and 'reversed' not in command.lower() and n != None and m == None):
        (do_next,command_output) = do_replay_n(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay reversed silent
    elif command_name.lower() =='replay' and 'reversed silent' in \
        command.lower() and n == None and m == None:
        (do_next,command_output) = do_replay_reversed_silent(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay reversed
    elif command_name.lower() =='replay' and 'reversed' in command.lower()\
        and 'silent' not in command.lower():
        # print(6)
        (do_next,command_output) = do_replay_reversed(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next
    # replay silent
    elif arg[0:6].lower() == 'silent' and command_name.lower() =='replay':
        if command == 'replay silent':
            (do_next,command_output) = do_replay_silent(robot_name,command)
            print(command_output)
            show_position(robot_name)
            return do_next
        else:
            print('wrong')
            return do_next
    # replay
    elif (command_name.lower() == 'replay' and 'silent' not in command.lower() \
        and 'reversed' not in command.lower() and n == None and m == None):
        (do_next,command_output) = do_replay(robot_name,command)
        print(command_output)
        show_position(robot_name)
        return do_next


def handle_command_replay(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command
    """

    (command_name, arg) = split_command_input(command)
    if command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
        print(command_output)
        show_position(robot_name)
        return do_next
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
        print(command_output)
        show_position(robot_name)
        return do_next
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
        print(command_output)
        show_position(robot_name)
        return do_next
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
        print(command_output)
        show_position(robot_name)
        return do_next
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
        print(command_output)
        show_position(robot_name)
        return do_next


def handle_command_replay_silent(robot_name, command):
    """echjv
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command
    """

    (command_name, arg) = split_command_input(command)
    if command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    # print(command_output)
    # show_position(robot_name)
    return do_next


def handle_command_replay_reversed(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command
    """

    (command_name, arg) = split_command_input(command)
    if command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    print(command_output)
    show_position(robot_name)
    return do_next


def handle_command_replay_reversed_silent(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command
    """

    (command_name, arg) = split_command_input(command)
    if command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    # print(command_output)
    # show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""
    global position_x, position_y, current_direction_index,history_list,digits,n,m
    history_list = []
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    position_x = 0
    position_y = 0
    current_direction_index = 0
    digits = None
    n = None
    m = None

    command = get_command(robot_name)

    while handle_command(robot_name, command):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()