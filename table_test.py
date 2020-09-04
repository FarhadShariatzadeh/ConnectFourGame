from table import Table


params = {
    'x': 0,
    'y': 200,
    'w': 1400,
    'h': 1200}


def test_constructor():

    a = Table(params['x'], params['y'],
              params['w'], params['h'])

    assert a.x == 0 and a.y == 200 and \
        a.w == 1400 and a.h == 1200 and \
        a.grid == [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


def test_get_empty_row_index():
    a = Table(params['x'], params['y'],
              params['w'], params['h'])

    a.grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]

    assert a.get_empty_row_index(2) == 2
    assert a.get_empty_row_index(1) == 5
