
import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg)        
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle

        for x in range(5, self.width - 75, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind("<Left>", lambda _: self.paddle.move(-10))
        self.canvas.bind("<Right>", lambda _: self.paddle.move(10))

    def setup_game(self):
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, "Press Space to start")
        self.canvas.bind("<space>", lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) / 2
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size="40"):
        font = ("Helvetica", size)
        return self.canvas.create_text(x, y, text=text, font=font)
    
    def update_lives_text(self):
        text = "Lives: %s" % self.lives
        if self.hud == None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        pass


    


class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)
    
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the ball
        self.radius = 10 
        self.direction[1, -1]    
        #This represents the speed of the ball in the x and y direction.  Example:  [xspeed, yspeed]
        self.speed = 10 
        x1 = x - self.radius
        y1 = y - self.radius
        x2 = x + self.radius
        y2 = y + self.radius
        color = "white"
        item = canvas.create_oval(x1, y1, x2, y2, fill=color)
        super(Ball, self).__init__(canvas, item)

class Paddle(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the paddle
        #YOUDO-09:  create a width variable for self and set to 80
        #YOUDO-10:  create a height variable for self and set to 10
        #YOUDO-11:  create a ball variable for self and set to None
        #YOUDO-12:  create an x1 variable and set to x - self's width / 2
        #YOUDO-13:  create an y1 variable and set to y - self's height / 2
        #YOUDO-14:  create an x2 variable and set to x + self's width / 2
        #YOUDO-15:  create an y2 variable and set to y + self's height / 2
        #YOUDO-16:  create a color variable and set to "blue"
        #YOUDO-17:  use create_rectangle on canvas to create an item variable with x1, y1, x2, y2, color
        super(Paddle, self).__init__(canvas, item)
        

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo.width()
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        if x1 + offset >= 0 and x2 + offset <= width:
            super(Paddle, self).move(offset, 0)
        if self.ball is not None:
            self.ball.move(offset, 0)

class Brick(GameObject):
    COLORS = {1 : "#999999", 2 : "#555555", 3 : "#222222"}

    def __init__(self, canvas, x, y, hits):
        #YOUDO-18:  create a width variable for self and initialize to 75
        #YOUDO-19:  create a height variable for self and initialize to 20
        #YOUDO-20:  create a hits variable for self and initialize to hits 
        color = Brick.COLORS[hits]
        #YOUDO-21:  create an x1 variable and set to x - self's width / 2
        #YOUDO-22:  create an y1 variable and set to y - self's height / 2
        #YOUDO-23:  create an x2 variable and set to x + self's width / 2
        #YOUDO-24:  create an y2 variable and set to y + self's height / 2
        #YOUDO-25:  use create_rectangle on canvas to create an item variable with x1, y1, x2, y2, color, tags="brick"        
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        self.hits - 1
        if self.hits == 0:
            self.delete()
        else: 
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])

if __name__ == "__main__":    
    root = tk.Tk()
    game = Game(root)
    root.title("BREAKOUT")
    root.mainloop()
