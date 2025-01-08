import pygame
import snd.constant as CONST
from snd.core import G2048,logger

class Game:
    """Game class"""

    def __new__(cls,width:int=4,height:int=4):
        logger.info("{:=^60}".format("GAME INITIALIZING"))
        return super().__new__(cls)

    def __init__(self,width:int=4,height:int=4) -> None:
        """Initialize the game"""
        self.run = True
        self.width = width
        self.height = height
        self.game = G2048(width,height)
        self.key :dict[int,bool]={}
        self.mouse :tuple[int,int] = (0,0)

    def __del__(self) -> None:
        """Delete the game"""
        logger.info("{:=^60}".format("GAME OVER"))

    def keydown(self,event:pygame.event.Event) -> None:
        """Handle key down event"""
        self.key[event.key] = True

    def keyup(self,event:pygame.event.Event) -> None:
        """Handle key up event"""
        if event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]:  
            match event.key:
                case pygame.K_UP:
                    self.game.move((0,-1))
                case pygame.K_DOWN:
                    self.game.move((0,1))
                case pygame.K_LEFT:
                    self.game.move((-1,0))
                case pygame.K_RIGHT:
                    self.game.move((1,0))
                case _:
                    pass
            self.run = self.game.check()
        self.key[event.key] = False

    def mouse_down(self,event:pygame.event.Event) -> None:
        """Handle mouse down event"""
        self.mouse = event.pos

    def mouse_up(self,event:pygame.event.Event) -> None:
        """Handle mouse up event"""
        right = event.pos[0]-self.mouse[0]
        down = event.pos[1]-self.mouse[1]
        logger.info(f"MOUSE MOVE : RIGTH = {right},DOWN = {down}")
        if abs(right)>abs(down):
            if right>CONST.MOVE_THRESHOLD:
                self.game.move((1,0))
            elif right<-CONST.MOVE_THRESHOLD:
                self.game.move((-1,0))
            else:
                return
        elif abs(right)<abs(down):
            if down>CONST.MOVE_THRESHOLD:
                self.game.move((0,1))
            elif down<-CONST.MOVE_THRESHOLD:
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