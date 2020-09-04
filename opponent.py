from table import Table
import random


class Opponent:
    ''' AI randomly make a yellow circle and drop it in the
    free spase in table'''

    def computer_make_move(self, table):
        column = -1  # It help to enter the while loop
        while column in table.full_columns or column < 0:
            column = random.randrange(7)
        self.x = column
        self.y = table.get_empty_row_index(self.x)
