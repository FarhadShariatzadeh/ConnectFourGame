from game_controller import GameController

SIZE = {'w': 1400, 'h': 1400}
playing = GameController()


def setup():
    size(SIZE['w'], SIZE['h'])
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
    elif answer == '':
        print('[empty string]')
    else:
        print(answer)  # Canceled dialog will print None
    playing.user_name = answer


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    background_color = 130
    background(background_color)
    playing.update()


def mousePressed():
    playing.handle_mousePressed()


def mouseDragged():
    playing.handle_mouseDragged()


def mouseReleased():
    playing.handle_mouseRealeased()
