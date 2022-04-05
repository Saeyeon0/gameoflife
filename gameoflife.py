from tkinter import *
from time import sleep
from random import randint, choice
from turtle import heading

# as a clue I used the code published as an example on OCS
# tried to illustrate characters in small heart shape
# men = blue
# women = pink
# their children = orange


class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        self.c = c
        self.a = []
        self.b = []
        self.n = n + 2
        self.m = m + 2
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            self.b.append([])
            for j in range(self.m):
                self.a[i].append(choice([0, 1]))
                self.a[i].append(0)
                self.b[i].append(0)
                if (randint(1, 11) == 1) and self.a[i][j] == 0:
                    self.a[i][j] = 1
                elif (randint(1, 7) == 1) and self.a[i][j] == 0:
                    self.a[i][j] = 2
                elif (randint(1, 5) == 1) and self.a[i][j] == 0:
                    self.a[i][j] = 3

        self.a[1+10][1+10] = 1
        self.a[1+10][3+10] = 1
        self.a[2+10][3+10] = 1
        self.a[2+10][2+10] = 1
        self.a[3+10][2+10] = 1
        self.draw()

    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)

        for i in range(1, self.n - 1):     # men
            for j in range(1, self.m - 1):
                self.a[i].append(choice([0, 1]))
                self.a[i].append(0)
                if self.a[i][j] == 1:
                    neib_sum = (self.a[i][j - 1] + self.a[i + 1]
                                [j - 1] + self.a[i + 1][j])
                    if neib_sum < 3 or neib_sum > 17:
                        b[i][j] = 0
                    elif neib_sum == 3:
                        b[i][j] = 1
                    else:
                        b[i][j] = self.a[i][j]

        for i in range(1, self.n - 1):     # women
            for j in range(1, self.m - 1):
                self.a[i].append(choice([0, 1]))
                self.a[i].append(0)
                if self.a[i][j] == 2:
                    neib_sum = (self.a[i - 1][j] + self.a[i - 1]
                                [j + 1] + self.a[i][j + 1])
                    if neib_sum < 3 or neib_sum > 17:
                        b[i][j] = 0
                    elif neib_sum == 3:
                        b[i][j] = 2
                    else:
                        b[i][j] = self.a[i][j]

        for i in range(1, self.n - 1):     # children
            for j in range(1, self.m - 1):
                self.a[i].append(choice([0, 1]))
                self.a[i].append(0)
                if self.a[i][j] == 3:
                    neib_sum = (self.a[i - 1][j - 1] + self.a[i - 1]
                                [j] + self.a[i - 1][j + 1])
                    if neib_sum < 3 or neib_sum > 17:
                        b[i][j] = 0
                    elif neib_sum == 3:
                        b[i][j] = 3
                    else:
                        b[i][j] = self.a[i][j]

        self.a = b

    def check_cell_neighbors(self, row_index, col_index):
        num_alive_neighbors = 0
        num_alive_neighbors += self.check_cells(row_index - 1, col_index - 1)
        num_alive_neighbors += self.check_cells(row_index - 1, col_index)
        num_alive_neighbors += self.check_cells(row_index - 1, col_index + 1)
        num_alive_neighbors += self.check_cells(row_index, col_index - 1)
        num_alive_neighbors += self.check_cells(row_index, col_index + 1)
        num_alive_neighbors += self.check_cells(row_index + 1, col_index - 1)
        num_alive_neighbors += self.check_cells(row_index + 1, col_index)
        num_alive_neighbors += self.check_cells(row_index + 1, col_index + 1)
        return num_alive_neighbors

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        color = "white"
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    color = "blue"
                elif (self.a[i][j] == 2):
                    color = "pink"
                elif (self.a[i][j] == 3):
                    color = "orange"
                else:
                    color = "sky blue"
                self.c.create_rectangle(
                    (i-1)*sizen, (j-1)*sizem, (i)*sizen, (j)*sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)

root = Tk()
root.geometry("800x800")
c = Canvas(root, width=800, height=800)
c.pack()

f = Field(c, 40, 40, 800, 800)
f.print_field()


root.mainloop()
