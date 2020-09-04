from table import Table
from opponent import Opponent

params = {
    'x': 0,
    'y': 200,
    'w': 1400,
    'h': 1200}


def test_computer_make_move():
    # Test The AI find a correct empty place

    a = Table(params['x'], params['y'],
              params['w'], params['h'])
    a.grid = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 2, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]
    a.get_empty_row_index(2)
    ai = Opponent()
    ai.computer_make_move(a)

    assert ai.x != 2
    assert ai.x not in a.full_columns
