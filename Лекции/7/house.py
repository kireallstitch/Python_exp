if __name__ == "__main__":
   main() 


def main():
    x, y = 100, 200
    width, height = 200, 300

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Нарисовать домик ширины width и высоты height от опорной точки(x, y),
    которая находится в середине нижней точки фундамента.
    :param x: коорд. x середины домика
    :param y: коорд. y  низа фундамента
    :param width: полная ширина домика (фундамент и вылет крыши вкл.)
    :param height: полная высота домика
    :return: None
    """
    print('Типа рисую домик...', x, y, width, height)
    foundation_height = 0.05 * height
    wall_height = 0.5 * height
    wall_width = 0.9 * width
    roof_height = height - foundation_height - wall_height

    draw_house_foundation(x, y, width,foundation_height)
    draw_house_walls(x, y - foundation_height, wall_height, wall_width)
    draw_house_roof(x, y - foundation_height - wall_height, width, roof_height)


def draw_house_foundation(x, y, width, height):
    """
    Нарисовать основание домика ширины width и высоты height от опорной точки(x, y),
    которая находится в середине нижней точки фундамента.
    :param x: коорд. x середины фундамента
    :param y: коорд. y  низа фундамента
    :param width: полная ширина фундамента (фундамент и вылет крыши вкл.)
    :param height: полная высота фундамента
    :return: None
    """
    print('Типа рисую основание...', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    print('Типа рисую стены...', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    print('Типа рисую крышу...', x, y, width, height)
    pass
 
 

main()
