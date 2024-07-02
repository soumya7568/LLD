from cell import Cell
import random
from jump import Jump

class Board:
    
    def __init__(self,n,snake,ladder) -> None:
        self.cells = [[0]*n for i in range(n)]
        self.n = n
        self.populate_cells(n)
        self.add_snake_and_ladder(n,snake,ladder)
        
        
    def populate_cells(self,n):
        for i in range(n):
            for j in range(n):
                self.cells[i][j] = Cell()
                
                
    def add_snake_and_ladder(self,n,snake_cnt,ladder_cnt):
        while snake_cnt>0:
            num1,num2 = random.randint(1,n*n-1),random.randint(1,n*n-1)
            if num1==num2:
                continue
            head = max(num1,num2)
            tail = min(num1,num2)
            snake = Jump(head,tail)
            cell = self.get_cell(head)
            if cell.jump:
                continue
            cell.jump = snake
            snake_cnt-=1
            
        while ladder_cnt>0:
            num1,num2 = random.randint(1,n*n-1),random.randint(1,n*n-1)
            if num1==num2:
                continue
            tail = max(num1,num2)
            head = min(num1,num2)
            ladder = Jump(head,tail)
            cell = self.get_cell(head)
            if cell.jump:
                continue
            cell.jump = ladder
            ladder_cnt-=1
            
    def get_cell(self,pos):
        row = pos//self.n
        col = pos%self.n
        return self.cells[row][col]
    