class Circle:
    '''A Circle'''
    def __init__(self, x, y, color_1, color_2, color_3):
        self.x = x
        self.y = y
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.rate = 0
        self.cap = 1300
        self.counter = 0
        self.seen = True

    def displayMe(self):
        if self.seen is True:
            size_circle = 200
            noStroke()
            fill(self.color_1, self.color_2, self.color_3)
            ellipse(self.x, self.y, size_circle, size_circle)
