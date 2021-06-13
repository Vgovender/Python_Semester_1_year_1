x_axis_pos = False
x_axis_neg = False
y_axis_pos = True
y_axis_neg = False

x_cordinate = 0
y_cordinate = 0

count = 0
def get_robot_name():
    name = input('What do you want to name your robot? ')
    print(name +': Hello kiddo!')
    return name

def get_command_input(name):
    command = input(name +': What must I do next? ')
    split_command = command.split(' ')#(sep = " ",maxsplit = 2)
    return split_command

def get_command_input_execute_steps(name,command_list,split_command):
    # length of input = 1
    if len(split_command) == 1:
        # off
        if split_command[0].upper() == command_list[0]:
            execute_command_off(name,command_list,split_command)
        # help
        elif split_command[0].upper() == command_list[1]:
            execute_command_help(name,command_list,split_command)
        # right
        elif split_command[0].upper() == command_list[4]:
            execute_command_right(name,command_list,split_command)
            split_command = get_command_input(name)
            get_command_input_execute_steps(name,command_list,split_command)
        # left
        elif split_command[0].upper() == command_list[5]:
            execute_command_left(name,command_list,split_command)
            split_command = get_command_input(name)
            get_command_input_execute_steps(name,command_list,split_command)
        # anything else
        else:
            if split_command[0].upper() not in command_list:
                print(name + ' Sorry, I did not understand \''+split_command[0]+'\'')
                split_command = get_command_input(name)
                get_command_input_execute_steps(name,command_list,split_command)
    # length of input = 2
    elif len(split_command) == 2 and isinstance(split_command[1],str) == True:
            # forward
            if split_command[0].upper() == command_list[2]:
                execute_command_forward(name,command_list,split_command)
                split_command = get_command_input(name)
                get_command_input_execute_steps(name,command_list,split_command)
            # back
            elif split_command[0].upper() == command_list[3]:
                execute_command_back(name,command_list,split_command)
                split_command = get_command_input(name)
                get_command_input_execute_steps(name,command_list,split_command)
            # sprint 
            elif split_command[0].upper() == command_list[6]:
                execute_command_sprint(name,command_list,split_command)
                split_command = get_command_input(name)
                get_command_input_execute_steps(name,command_list,split_command)
            else:
                print(name + ': Sorry, I did not understand \''+split_command[0]+' '+split_command[1]+'\'.')
                split_command = get_command_input(name)
                get_command_input_execute_steps(name,command_list,split_command)

def execute_command_off(name,command_list,split_command):
    print(name +': Shutting down..')

def execute_command_help(name,command_list,split_command):
    print('I can understand these commands:')
    print(command_list[0] + '  - Shut down robot')
    print(command_list[1] + ' - provide information about commands')
    print(command_list[2] + ' - moves the robot forward from current position')
    print(command_list[3] + ' - moves the robot back from current position')
    print(command_list[4] + ' - turns the robot right')
    print(command_list[5] + ' - turns the robot left')
    print(command_list[6] + ' - robot sprints')
    print('')
    split_command = get_command_input(name)
    get_command_input_execute_steps(name,command_list,split_command)

def execute_command_forward(name,command_list,split_command):
    track_position(name,command_list,split_command)

def execute_command_back(name,command_list,split_command):
    track_position(name,command_list,split_command)

def execute_command_right(name,command_list,split_command):
    global x_cordinate
    global y_cordinate
    print(' > '+ name +' turned right.')
    get_direction(command_list,split_command)
    print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')

def execute_command_left(name,command_list,split_command):
    global x_cordinate
    global y_cordinate
    print(' > '+ name +' turned left.')
    get_direction(command_list,split_command)
    print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')

def execute_command_sprint(name,command_list,split_command):
    global x_cordinate
    global y_cordinate
    global count
    steps = int(split_command[1])
    while steps != 0:
        count += steps
        print(' > '+ name +' moved forward by '+ str(steps) +' steps.')
        steps -= 1
    execute_command_forward(name,command_list,split_command)


def get_direction(command_list,split_command):
    global x_axis_pos
    global x_axis_neg
    global y_axis_pos
    global y_axis_neg
    # right
    if split_command[0].upper() == command_list[4] and x_axis_pos == True:
        x_axis_pos = False
        x_axis_neg = False
        y_axis_pos = False
        y_axis_neg = True
        # print('y_axis_neg')
    elif split_command[0].upper() == command_list[4] and y_axis_neg == True:
        x_axis_pos = False
        x_axis_neg = True
        y_axis_pos = False
        y_axis_neg = False
        # print('x_axis_neg')
    elif split_command[0].upper() == command_list[4] and x_axis_neg == True:
        x_axis_pos = False
        x_axis_neg = False
        y_axis_pos = True
        y_axis_neg = False
        # print('y_axis_pos')
    elif split_command[0].upper() == command_list[4] and y_axis_pos == True:
        x_axis_pos = True
        x_axis_neg = False
        y_axis_pos = False
        y_axis_neg = False
        # print('x_axis_pos')
    # left
    if split_command[0].upper() == command_list[5] and x_axis_pos == True:
        x_axis_pos = False
        x_axis_neg = False
        y_axis_pos = True
        y_axis_neg = False
        # print('y_axis_pos')
    elif split_command[0].upper() == command_list[5] and y_axis_pos == True:
        x_axis_pos = False
        x_axis_neg = True
        y_axis_pos = False
        y_axis_neg = False
        # print('x_axis_neg')
    elif split_command[0].upper() == command_list[5] and x_axis_neg == True:
        x_axis_pos = False
        x_axis_neg = False
        y_axis_pos = False
        y_axis_neg = True
        # print('y_axis_neg')
    elif split_command[0].upper() == command_list[5] and y_axis_neg == True:
        x_axis_pos = True
        x_axis_neg = False
        y_axis_pos = False
        y_axis_neg = False
        # print('x_axis_pos')

def track_position(name,command_list,split_command):
    global x_axis_pos
    global x_axis_neg
    global y_axis_pos
    global y_axis_neg
    global x_cordinate
    global y_cordinate
    global count
    y_cordinate_temp = 0
    x_cordinate_temp = 0
    # (0,0)
    # robot currently facing x_axis_pos
    # range for x
    x_cordinate_temp = int(split_command[1])
    y_cordinate_temp = int(split_command[1])
    # forward
    if split_command[0].upper() == command_list[2] or split_command[0].upper() == command_list[6]:
        if x_cordinate_temp >= 100 or x_cordinate_temp < -100:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_cordinate_temp >= 200 or y_cordinate_temp < -200:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif x_axis_pos == True and x_cordinate <= 100:
            if split_command[0].upper() == command_list[6]:
                x_cordinate += count
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
            if split_command[0].upper() == command_list[2]:
                x_cordinate += x_cordinate_temp
                print(' > '+ name +' moved forward by '+ split_command[1] +' steps.')
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif x_axis_pos == True and (x_cordinate > 100 or x_cordinate_temp > 100):
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif x_axis_neg == True and x_cordinate >= -100:
            if split_command[0].upper() == command_list[6]:
                x_cordinate += count
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
            if split_command[0].upper() == command_list[2]:
                x_cordinate -= x_cordinate_temp
                print(' > '+ name +' moved forward by '+ split_command[1] +' steps.')
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif x_axis_neg == True and x_cordinate < -100:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_pos == True and y_cordinate <= 200:
            if split_command[0].upper() == command_list[6]:
                y_cordinate += count
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
            if split_command[0].upper() == command_list[2]:
                y_cordinate += y_cordinate_temp
                print(' > '+ name +' moved forward by '+ split_command[1] +' steps.')
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_pos == True and y_cordinate > 200:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_neg == True and y_cordinate >= -200:
            if split_command[0].upper() == command_list[6]:
                y_cordinate += count
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
            if split_command[0].upper() == command_list[2]:
                y_cordinate -= y_cordinate_temp
                print(' > '+ name +' moved forward by '+ split_command[1] +' steps.')
                print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
            # y_cordinate -= y_cordinate_temp
            # print(' > '+ name +' moved forward by '+ split_command[1] +' steps.')
            # print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_neg == True and y_cordinate < -200:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
    # back
    elif split_command[0].upper() == command_list[3]:
        if x_axis_pos == True and x_cordinate <= 100:
            x_cordinate -= x_cordinate_temp
            print(' > '+ name +' moved back by '+ split_command[1] +' steps.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif x_axis_pos == True and x_cordinate <= -100:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif x_axis_neg == True and x_cordinate >= -100:
            x_cordinate += x_cordinate_temp
            print(' > '+ name +' moved back by '+ split_command[1] +' steps.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif x_axis_neg == True and x_cordinate < 100:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_pos == True and y_cordinate <= 200:
            y_cordinate -= y_cordinate_temp
            print(' > '+ name +' moved back by '+ split_command[1] +' steps.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_pos == True and y_cordinate > -200:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_neg == True and y_cordinate >= -200:
            y_cordinate += y_cordinate_temp
            print(' > '+ name +' moved back by '+ split_command[1] +' steps.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        elif y_axis_neg == True and y_cordinate < -200:
            print(name+': Sorry, I cannot go outside my safe zone.')
            print(' > '+ name +' now at position ('+str(x_cordinate)+','+str(y_cordinate)+').')
        

def robot_start():
    """This is the entry function, do not change"""
    global x_axis_neg,x_axis_pos,y_axis_pos,y_axis_neg
    global x_cordinate
    global y_cordinate
    global x_axis_neg,x_axis_pos,y_axis_pos,y_axis_neg
    name = get_robot_name()
    command_list = ['OFF','HELP','FORWARD','BACK','RIGHT','LEFT','SPRINT']
    split_command = get_command_input(name)
    get_command_input_execute_steps(name,command_list,split_command)
    
    x_axis_pos = False
    x_axis_neg = False
    y_axis_pos = True
    y_axis_neg = False
    x_cordinate = 0
    y_cordinate = 0


if __name__ == "__main__":
    robot_start()
