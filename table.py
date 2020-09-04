

class Table:
    def __init__(self, tempX, tempY, tempW, tempH):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH
        row = 6
        column = 7
        # grid is a list of list to store the place of circle in it.
        # and access to the location of each of the circle.
        self.grid = [[0] * column for i in range(row)]
        self.full_columns = set()

    def display(self):
        blue_color = 255
        gray_color = 130
        strokeweigh_number = 30
        stroke(0, 0, blue_color)
        line_size = 200
        fill(gray_color, gray_color, gray_color)
        strokeWeight(strokeweigh_number)
        line(0, line_size, 0, line_size*7)
        line(0, line_size*2, line_size*7, line_size*2)
        line(0, line_size*3, line_size*7, line_size*3)
        line(0, line_size*4, line_size*7, line_size*4)
        line(0, line_size*5, line_size*7, line_size*5)
        line(0, line_size*6, line_size*7, line_size*6)
        line(line_size*7, line_size, line_size*7, line_size*7)

        line(0, line_size, line_size*7, line_size)
        line(line_size, line_size, line_size, line_size*7)
        line(line_size*2, line_size, line_size*2, line_size*7)
        line(line_size*3, line_size, line_size*3, line_size*7)
        line(line_size*4, line_size, line_size*4, line_size*7)
        line(line_size*5, line_size, line_size*5, line_size*7)
        line(line_size*6, line_size, line_size*6, line_size*7)
        line(0, line_size*7, line_size*7, line_size*7)

    def get_empty_row_index(self, column):
        # find empty place in the grid to place the circle. it start looking
        # for the empty place in the grid from the bottom and return it.
        empty_index = 0
        for i in range(len(self.grid)-1, -1, -1):
            if self.grid[i][column] == 0:
                empty_index = i
                break
        # When a column is full and no place for more circles, add the column
        # to set.
        if empty_index == 0:
            self.full_columns.add(column)
        return empty_index
