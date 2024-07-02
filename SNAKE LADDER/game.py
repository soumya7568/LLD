from collections import deque
from board import Board
from dice import Dice
from player import Player

class Game:
    
    def __init__(self) -> None:
        self.dice = Dice(1)
        self.board = Board(10,5,4)
        self.winner = None
        self.queue = deque()
        self.add_players()
        
    def add_players(self):
        for i in range(2):
            player = Player(i)
            self.queue.append(player)
            
    def start_game(self):
        while not self.winner:
            player = self.queue.popleft()
            print(f"Now player{player.user_id}'s turn and his current position is {player.position}")
            
            dice_number = self.dice.roll_dice()
            print(f"the number in dice is {dice_number}")
            
            new_pos = player.position + dice_number
            new_pos = self.jump_check(new_pos)
            print(f"player new position is {new_pos}")
            player.position = new_pos
            if new_pos>= self.board.n * self.board.n:
                self.winner = f"player{player.user_id}"
            self.queue.append(player)
            
        print(f"******************** Winner is  {self.winner} **********************")
        return
        
    def jump_check(self,pos):
        if pos>=self.board.n * self.board.n:
            return pos
        
        cell = self.board.get_cell(pos)
        if cell.jump and cell.jump.start==pos:
            jumpby = "ladder" if cell.jump.end > cell.jump.start else "ladder"
            print(f"player is jumping by {jumpby}")
            return cell.jump.end
        
        return pos
        
        
        
        