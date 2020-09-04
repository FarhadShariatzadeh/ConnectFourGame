from circle import Circle


params = {
    'x': 300,
    'y': 100,
    'color_1': 255,
    'color_2': 0,
    'color_3': 0
}


def test_constructor():
    # Test minimal required constructor args
    a = Circle(params['x'], params['y'], params['color_1'],
               params['color_2'], params['color_3'])

    assert a.x == params['x'] and a.y == params['y'] and \
        a.color_1 == params['color_1'] and \
        a.color_2 == params['color_2'] and \
        a.color_3 == params['color_3'] and \
        a.rate == 0 and a.cap == 1300
