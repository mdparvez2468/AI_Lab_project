import turtle as tl
import tkinter.messagebox as tmsg
import numpy as np
class BFS:
    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.n = self.x * self.y
        self.matrix = np.zeros((self.n, self.n))

    def adjacency(self, prohibited):
        for i in range(self.n):
            if i not in prohibited:
                for j in range(self.n):
                    if j == i + self.x or j == i - self.x:
                        self.matrix[i][j] = 1
                    if i % self.x == 0:
                        if j == i + 1:
                            self.matrix[i][j] = 1
                    elif (i + 1) % self.x == 0:
                        if j == i - 1:
                            self.matrix[i][j] = 1
                    else:
                        if j == i + 1 or j == i - 1:
                            self.matrix[i][j] = 1

    def calculate_distance(self, m, n):
        self.visited = np.zeros(self.n)
        self.parent = np.zeros(self.n)
        self.visited[m] = 1
        self.queue = []
        self.queue.append(m)
        while len(self.queue) > 0:
            a = self.queue[0]
            self.queue.remove(a)
            for i in range(self.n):
                if self.matrix[a][i] == 1 and self.visited[i] == 0:
                    self.parent[i] = a
                    self.visited[i] = 1
                    self.queue.append(i)
                    if i == n:
                        self.queue = []
                        break
        if i != n:
            return
        self.traversed = []
        p = int(self.parent[n])
        self.traversed.append(p)
        while (p != m):
            p = int(self.parent[p])
            if p == m:
                break
            self.traversed.append(p)


class Body:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.screen = tl.Screen()
        self.screen.setup(self.width, self.height)
        self.screen.title("Optimal Path - AI_Lab_project")
        self.screen.bgcolor("white")
        self.x = 0
        self.y = 0
        self.run = True
        self.dx = 48
        self.dy = 20
        self.step = 20
        self.cy = 110
        self.cx = -470
        self.prohibited = []
        self.rs = []
        self.write()
        self.grid()
        self.allow = True
        # self.main()
        self.hs = []
        self.start_pt = 0
        self.end_pt = 959
        self.start = True
        self.end = False
        self.hurdles = False
        self.listen_mouse_clicks()
        self.screen.mainloop()

    def main(self):
        b = BFS(self.dx, self.dy)
        b.adjacency(self.prohibited)
        try:
            b.calculate_distance(self.start_pt, self.end_pt)
            for i in self.rs:
                i.goto(1000, 1000)
            self.rs.clear()
            for i in b.traversed:
                self.draw_point(i)
        except:
            tmsg.showinfo("Not Found", "No path found between between the start and the end points")

    def draw_point(self, n):
        self.block = tl.Turtle()
        self.block.penup()
        self.block.shape("square")
        self.block.color("black")
        self.block.speed(0)
        self.block.goto(self.cx + 20 * (n % self.dx), self.cy - 20 * (n // self.dx))
        self.rs.append(self.block)

    def draw_start(self):
        self.start = True
        self.end = False
        self.hurdles = False

    def draw_end(self):
        self.start = False
        self.end = True
        self.hurdles = False

    def draw_mark(self):
        self.start = False
        self.end = False
        self.hurdles = True

    def write(self):
        self.pen = tl.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("red")
        self.pen.goto(-480, 300)
        self.pen.write(" Group Members", False,
            align="left", font=("arial",20, "bold"))
        self.pen.goto(-480, 250)
        self.pen.write("1. Md Parvez (191-15-2468)", False,
            align="left", font=("arial", 15, "bold"))
        self.pen.goto(-480, 210)
        self.pen.write("2. Meherunnessa Samia (191-15-2456)", False,
            align="left", font=("arial", 15, "bold"))
        self.pen.goto(-480, 170)
        self.pen.write("3. Israt Jahan Shoshe (191-15-2474)", False,
            align="left", font=("arial", 15, "bold"))
        self.pen.goto(-480, 130)
        self.pen.write("{ Press 's' for the starting point, 'e' for end, 'm' for mark,space for finding path and 'c' for clear than click anywhere}", False,
            align="left", font=("arial", 10, "bold"))


    def draw_squares(self, x, y):
        xcor = None
        ycor = None
        for i in range(self.dx):
            if x < (self.cx + 20 * i) + 10 and x > (self.cx + 20 * i) - 10:
                xcor = self.cx + 20 * i
                break
        for j in range(self.dy):
            if y < (self.cy - 20 * j) + 10 and y > (self.cy - 20 * j) - 10:
                ycor = self.cy - 20 * j
                break
        if self.hurdles:
            if xcor and ycor:
                loc = j * self.dx + i
                self.prohibited.append(loc)
                self.t = tl.Turtle()
                self.t.penup()
                self.t.shape("square")
                self.t.color("red")
                self.t.speed(-1)
                self.t.goto(xcor, ycor)
                self.hs.append(self.t)
        if self.start:
            if xcor and ycor:
                self.start_pt = j * self.dx + i
                try:
                    self.st.goto(xcor, ycor)
                except:
                    self.st = tl.Turtle()
                    self.st.penup()
                    self.st.shape("square")
                    self.st.color("green")
                    self.st.speed(-1)
                    self.st.goto(xcor, ycor)
        if self.end:
            if xcor and ycor:
                self.end_pt = j * self.dx + i
                try:
                    self.et.goto(xcor, ycor)
                except:
                    self.et = tl.Turtle()
                    self.et.penup()
                    self.et.shape("square")
                    self.et.color("blue")
                    self.et.speed(-1)
                    self.et.goto(xcor, ycor)

    def clear_all(self):
        try:
            self.et.goto(1000, 1000)
            self.st.goto(1000, 1000)
            for i in self.hs:
                i.goto(1000, 1000)
            self.hs = []
            self.prohibited = []
            for i in self.rs:
                i.goto(1000, 1000)
            self.rs = []
        except:
            pass
    def listen_mouse_clicks(self):
        self.screen.listen()
        self.screen.onclick(self.draw_squares)
        self.screen.onkeypress(self.main, "space")
        self.screen.onkeypress(self.draw_start, "s")
        self.screen.onkeypress(self.draw_end, "e")
        self.screen.onkeypress(self.draw_mark, "m")
        self.screen.onkeypress(self.clear_all, "c")


    def grid(self):
        self.g = tl.Turtle()
        self.g.color("red")
        self.g.hideturtle()
        self.g.speed(-1)
        for i in range(21):
            self.g.penup()
            self.g.goto(-480, +120 - (20 * i))
            self.g.pendown()
            self.g.forward(480 * 2)
        for i in range(49):
            self.g.penup()
            self.g.setheading(-90)
            self.g.goto(-480 + 20 * i, +120)
            self.g.pendown()
            self.g.forward(400)
b = Body()