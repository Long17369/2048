import pygame
import snd.constant as CONST
from snd.core import G2048

class Game:
    """Game class"""
    def __init__(self,width:int=4,height:int=4,is_print:bool=False) -> None:
        """Initialize the game"""
        self.run = True
        self.width = width
        self.height = height
        self.is_print = is_print
        self.game = G2048(width,height,is_print)
        self.key :dict[int,bool]={}
        self.mouse :tuple[int,int] = (0,0)

    def keydown(self,event:pygame.event.Event) -> None:
        """Handle key down event"""
        self.key[event.key] = True

    def keyup(self,event:pygame.event.Event) -> None:
        """Handle key up event"""
        self.key[event.key] = False

    def mouse_down(self,event:pygame.event.Event) -> None:
        """Handle mouse down event"""
        self.mouse = event.pos

    def mouse_up(self,event:pygame.event.Event) -> None:
        """Handle mouse up event"""
        right = event.pos[0]-self.mouse[0]
        down = event.pos[1]-self.mouse[1]
        print(right,down)
        if abs(right)>abs(down):
            if right>CONST.MOVE_THRESHOLD:
                print("right")
                self.game.move((1,0))
            elif right<-CONST.MOVE_THRESHOLD:
                print("left")
                self.game.move((-1,0))
            else:
                return
        elif abs(right)<abs(down):
            if down>CONST.MOVE_THRESHOLD:
                print("down")
                self.game.move((0,1))
            elif down<-CONST.MOVE_THRESHOLD:
                print("up")
                self.game.move((0,-1))
            else:
                return
        else:
            return

    def update(self) -> None:
        """Update the game"""
        a = [(k,v) for k,v in self.key.items()]
        for k,v in a:
            if v==False:
                print(k)
                self.key.pop(k)

if __name__ == "__main__":
    game = Game()
else:
    print("snd.game imported")