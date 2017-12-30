"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.
Example
For n = 3, the output should be
spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] integer n
    Matrix size, a positive integer.
    Guaranteed constraints:
    3 ≤ n ≤ 10.
    [output] array.array.integer
"""

class Obj(object):
    def __init__(self, n):
        self.matrix = [[0] * n for _ in range(n)]
        self.left, self.right, self.up, self.down = range(4)
        self.x, self.y = 0, -1
        self.way = self.right
        self.shiftCount = 0
    
    def moveForward(self):
        if self.way is self.right: self.y += 1
        elif self.way is self.down: self.x += 1
        elif self.way is self.left: self.y -= 1
        else: self.x -= 1

    def moveBackward(self):
        if self.way is self.right: self.y -= 1
        elif self.way is self.down: self.x -= 1
        elif self.way is self.left: self.y += 1
        else: self.x += 1
    
    def shiftRight(self):
        if self.way is self.right: self.way = self.down
        elif self.way is self.down: self.way = self.left
        elif self.way is self.left: self.way = self.up
        else: self.way = self.right
    
    def hitWall(self, n):
        if self.x == n or self.y == n: return True
        return True if self.matrix[self.x][self.y] != 0 else False

def spiralNumbers(n):
    obj, done, i = Obj(n), False, 1
    while not done:
        obj.moveForward()
        if not obj.hitWall(n):
            obj.shiftCount = 0
            obj.matrix[obj.x][obj.y] = i
            i += 1
        else:
            obj.shiftCount += 1
            obj.moveBackward()
            obj.shiftRight()
        if obj.shiftCount >= 2: done = True
    return obj.matrix