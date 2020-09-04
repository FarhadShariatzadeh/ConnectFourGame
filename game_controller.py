from circle import Circle
from table import Table
from opponent import Opponent
from score import Score


class GameController:
    '''Manitain the state of the game and manage
    how the game work'''

    def __init__(self):
        '''Iniitalize the game controller'''
        line_size = 200
        self.table = Table(0, line_size, line_size*7, line_size*6)
        self.circles = []
        self.winner_color = -1
        self.opponent = Opponent()
        self.winner = 0
        self.can_drop = True
        self.mouse_drag = False
        self.mouse_release = False
        self.mouse_pressed = True
        self.user_name = ""
        self.score = Score("scores.txt")
        self.txt_update_called = True
        self.game_over = False
        self.computer_turn = False
        self.winner_counter = 0

    def update(self):
        '''Updates game state on every frame'''
        text_size_number = 100
        size_circle = 200
        fill_number = 4
        yellow_number = 255
        counter_max = 90
        for i in self.circles:
            if i.color_2 == yellow_number:
                # It cause the yellow circle drope after a while
                if i.counter < counter_max:
                    i.counter = i.counter + 1
                    continue
            if i.x < size_circle:
                i.x = size_circle // 2
            elif i.x >= size_circle and i.x < size_circle*2:
                i.x = size_circle + size_circle/2
            elif i.x >= size_circle*2 and i.x < size_circle*3:
                i.x = size_circle*2 + size_circle/2
            elif i.x >= size_circle*3 and i.x < size_circle*4:
                i.x = size_circle*3 + size_circle/2
            elif i.x >= size_circle*4 and i.x < size_circle*5:
                i.x = size_circle*4 + size_circle/2
            elif i.x >= size_circle*5 and i.x < size_circle*6:
                i.x = size_circle*5 + size_circle/2
            else:
                i.x = size_circle*6 + size_circle/2
            i.displayMe()
            if i.y <= i.cap and self.can_drop:
                i.y = min(i.cap, i.y + i.rate)
                i.rate = i.rate + 5
        if len(self.circles) > 0:
            if self.circles[-1].color_2 == yellow_number and \
             self.circles[-1].y >= self.circles[-1].cap:
                self.mouse_pressed = True
                self.computer_turn = False
        self.table.display()
        if self.winner == 1:
            if self.winner_counter < counter_max:
                self.winner_counter = self.winner_counter + 1
                return
            if self.txt_update_called:
                self.update_txtfile()
                self.txt_update_called = False
            fill(fill_number)
            textSize(text_size_number)
            if self.winner_color == 0:
                string_text = "Red won!"
            else:
                string_text = "Yellow won!"
            text(string_text, text_size_number*5, text_size_number
                 + text_size_number/2)
            return
        if self.game_over is True:
            fill(fill_number)
            textSize(text_size_number)
            string_text = "Game Over!"
            text(string_text, text_size_number*5, text_size_number
                 + text_size_number/2)
            return
        if self.computer_turn:
            fill(fill_number*4)
            textSize(text_size_number/2)
            string_text = "computer's turn"
            text(string_text, text_size_number*10, text_size_number
                 + text_size_number/2)
        elif self.computer_turn is False:
            fill(fill_number*4)
            textSize(text_size_number/2)
            string_text = "your turn"
            text(string_text, text_size_number*10, text_size_number +
                 text_size_number/2)

    def handle_mousePressed(self):
        '''Add the circle to the game'''
        x_number = 200
        color_number = 255
        if self.mouse_pressed is False:
            return
        if mouseY > x_number:
            self.mouse_drag = False
            self.mouse_release = False
            return
        if self.winner == 0:
            column = mouseX//x_number
            if column in self.table.full_columns:
                return
            else:
                self.can_drop = False
                circle = Circle(mouseX, x_number//2, color_number, 0, 0)
                self.circles.append(circle)
                self.mouse_drag = True
                self.mouse_release = True

    def handle_mouseDragged(self):
        '''move the circle befor it release'''
        x_number = 200
        if self.mouse_drag is False or self.mouse_pressed is False:
            return
        if self.winner == 0:
            if (mouseX > x_number * 7 or mouseX < 0 or mouseY > x_number or
               mouseY < 0):
                self.circles[-1].seen = False
                self.mouse_release = False
                return
            else:
                self.circles[-1].seen = True
                self.mouse_release = True
            column = mouseX//x_number
            if column not in self.table.full_columns:
                self.circles[-1].x = mouseX
                self.mouse_release = True

    def handle_mouseRealeased(self):
        '''Droped the circle after mouse released'''
        x_number = 200
        if self.mouse_pressed is False:
            return
        if self.mouse_release is False:
            if self.mouse_drag is True:
                self.circles.pop()
            return
        if self.winner == 0:
            index_column = mouseX // x_number
            empty_row = self.table.get_empty_row_index(index_column)
            self.circles[-1].x = mouseX
            self.circles[-1].cap = empty_row * x_number + (x_number + x_number//2)
            self.table.grid[empty_row][index_column] = 1
            self.can_drop = True
            self.win(empty_row, index_column, self.circles[-1].color_2)
            if len(self.table.full_columns) == 7:
                self.game_over = True
            if self.winner == 0 and self.game_over is False:
                self.make_yellow_circle()
            self.computer_turn = True

    def make_yellow_circle(self):
        '''make yellow circle and decide when it droped'''
        color_number = 255
        x_number = 200
        self.mouse_pressed = False
        self.mouse_drag = False
        self.mouse_release = False
        self.opponent.computer_make_move(self.table)
        x = self.opponent.x
        circle = Circle(x*x_number, x_number//2, color_number, color_number, 0)
        self.circles.append(circle)
        self.circles[-1].cap = self.opponent.y * x_number + (x_number + x_number//2)
        self.table.grid[self.opponent.y][self.opponent.x] = 2
        self.win(self.opponent.y, self.opponent.x, self.circles[-1].color_2)

    def win(self, y_pos, x_pos, winner_color):
        '''described all the rulles for circles. If place four of circles with
        the same color in a row either horizontally, vertically, or diagonally
        that color win the game'''
        list_direction = [1] * 8
        color = self.table.grid[y_pos][x_pos]
        for i in range(1, 4):
            if (x_pos + i) >= len(self.table.grid[0]):
                list_direction[1] = 0
                list_direction[2] = 0
                list_direction[3] = 0
            if (y_pos + i) >= len(self.table.grid):
                list_direction[3] = 0
                list_direction[4] = 0
                list_direction[5] = 0
            if (x_pos - i) < 0:
                list_direction[5] = 0
                list_direction[6] = 0
                list_direction[7] = 0
            if (y_pos - i) < 0:
                list_direction[0] = 0
                list_direction[1] = 0
                list_direction[7] = 0
            if (list_direction[0] == 1):
                if (self.table.grid[y_pos - i][x_pos] != color):
                    list_direction[0] = 0
            if (list_direction[1] == 1):
                if i == 3:
                    if ((y_pos + 1) < len(self.table.grid) and
                       (x_pos - 1) >= 0):
                        if (self.table.grid[y_pos + 1][x_pos - 1] == color):
                            break
                if(self.table.grid[y_pos - i][x_pos + i] != color):
                    list_direction[1] = 0
            if (list_direction[2] == 1):
                if i == 3:
                    if((x_pos - 1) >= 0):
                        if (self.table.grid[y_pos][x_pos - 1] == color):
                            break
                if(self.table.grid[y_pos][x_pos + i] != color):
                    list_direction[2] = 0
            if (list_direction[3] == 1):
                if i == 3:
                    if((y_pos - 1) >= 0 and (x_pos - 1) >= 0):
                        if (self.table.grid[y_pos - 1][x_pos - 1] == color):
                            break
                if(self.table.grid[y_pos + i][x_pos + i] != color):
                    list_direction[3] = 0
            if (list_direction[4] == 1):
                if(self.table.grid[y_pos + i][x_pos] != color):
                    list_direction[4] = 0
            if (list_direction[5] == 1):
                if i == 3:
                    if((x_pos + 1) < len(self.table.grid[0]) and
                       (y_pos - 1) >= 0):
                        if (self.table.grid[y_pos - 1][x_pos + 1] == color):
                            break
                if(self.table.grid[y_pos + i][x_pos - i] != color):
                    list_direction[5] = 0
            if (list_direction[6] == 1):
                if i == 3:
                    if((x_pos + 1) < len(self.table.grid[0])):
                        if (self.table.grid[y_pos][x_pos + 1] == color):
                            break
                if (self.table.grid[y_pos][x_pos - i] != color):
                    list_direction[6] = 0
            if (list_direction[7] == 1):
                if i == 3:
                    if((x_pos + 1) < len(self.table.grid[0]) and
                       (y_pos + 1) < len(self.table.grid)):
                        if (self.table.grid[y_pos + 1][x_pos + 1] == color):
                            break
                if (self.table.grid[y_pos - i][x_pos - i] != color):
                    list_direction[7] = 0

        for i in list_direction:
            if i == 1:
                self.winner = 1
                self.winner_color = winner_color

    def update_txtfile(self):
        # When the user win, winner's name add to the score.txt

        if self.winner == 1 and self.winner_color == 0:
            self.score.write_name(self.user_name)
