

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ")
    shape_lower = shape.lower()
    while True:
        if shape_lower == "pyramid":
            return shape_lower
        elif shape_lower == "square":
            return shape_lower
        elif shape_lower == "triangle":
            return shape_lower
        elif shape_lower == "parallelogram":
            return shape_lower
        elif shape_lower == "rectangle":
            return shape_lower
        elif shape_lower == "right triangle":
            return shape_lower
        else:
            return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    while True:
        height = input("Height?: ")
        max = 80
        if height.isdigit():
            int_height = int(height)
        else:
            return get_height()
        if int_height > 0 and int_height <= 80:
            return int_height
        else:
            return get_height()


# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == 1:
        space = height -1
        inside_space = 1
        stars = 1
        print(' ' * space + '*' * stars)
        for x in range(height-2):
            print((' '* (space-1)) + '*' * stars + ' ' * inside_space + '*' * stars)
            space = space - 1
            inside_space = inside_space + 2
        print(('*' * stars)* ((height*2)-1))
    else:
        space = height - 1
        stars = 1
        for x in range(height):
            print(' ' * space + '*' * stars)
            space = space - 1
            stars = stars + 2


# TODO: Step 3
def draw_square(height, outline):
    if outline == 1:
        stars = 1
        space = 1
        print('*' * (stars*height))
        for x in range(height -2):
            print('*' * stars + ' ' * ((space*height)-2) + '*' * stars)
        print('*' * (stars*height))
    else:
        num = 0
        while num < height:
            num += 1
            print("*" * height)

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == 1:
        stars = 1
        space = 0
        print('*' * (stars))
        for x in range(height - 2):
            print('*' * stars + ' ' * (space) + '*' * stars)
            space = space + 1
        print('*' * (stars*height))
    else:
        num = 0
        while num < height:
            num += 1
            print("*" * num)

#shape 4
def draw_parallelogram(height, outline):
    if outline == 1:
        stars = 1
        space = (height)
        inside_space = height
        print(' ' * (space-1) + '*' * (stars*height))
        for x in range(height -2):
            print(' ' * (space-2) + '*' * stars + ' ' * (inside_space-2) + '*' * stars)
            space = space - 1
        print('*' * (stars*height))
    else:
        stars = 1
        space = (height)
        inside_space = height
        print(' ' * (space-1) + '*' * (stars*height))
        for x in range(height -2):
            print(' ' * (space-2) + '*' * stars + '*' * (inside_space-2) + '*' * stars)
            space = space - 1
        print('*' * (stars*height))

#shape 5
def draw_rectangle(height, outline):
    if outline == 1:
        stars = 1
        space = 1
        print('*' * ((stars*height)*3))
        for x in range(height -2):
            print('*' * stars + ' ' * (((space*height)*3)-2) + '*' * stars)
        print('*' * ((stars*height)*3))
    else:
        stars = 1
        space = 1
        print('*' * ((stars*height)*3))
        for x in range(height -2):
            print('*' * stars + '*' * (((space*height)*3)-2) + '*' * stars)
        print('*' * ((stars*height)*3))

#shape 6
def draw_right_triangle(height, outline):
    if outline == 1:
        stars = 1
        space = height-2
        inside_space = 0
        print(' ' * (space+1) + '*' * (stars))
        for x in range(height - 2):
            print(' ' * (space) +'*' * stars + ' ' * (inside_space) + '*' * stars)
            space = space - 1
            inside_space += 1
        print('*' * (stars*height))
    else:
        stars = 1
        space = height-2
        inside_space = 0
        print(' ' * (space+1) + '*' * (stars))
        for x in range(height - 2):
            print(' ' * (space) +'*' * stars + '*' * (inside_space) + '*' * stars)
            space = space - 1
            inside_space += 1
        print('*' * (stars*height))


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "parallelogram":
        draw_parallelogram(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)
    elif shape == "right triangle":
        draw_right_triangle(height, outline)



# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    while True:
        ans = input("Outline only? (y/N):")
        ans_low = ans.lower()
        if ans_low == "y":
            return True
        elif ans_low == "n":
            return False
        else:
            get_outline()


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

